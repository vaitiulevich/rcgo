import random

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_304_NOT_MODIFIED, HTTP_201_CREATED, HTTP_200_OK

from .models import User
from .serializers import UserCreateSerializer, UserInfoSerializer
from .tasks import send_mail_password_change, send_mail_password_reset, send_mail_registration


def random_password():
    chars = list("1234567890qwertyuiopasdfghjklzxcvbnm")
    password = ''
    for i in range(8):
        password += chars[random.randint(0, len(chars) - 1)]
    return password


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def info(request):
    if request.method == 'GET':
        params = request.query_params
        try:
            user = User.objects.get(pk=params.get('user'))
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def user(request):
    if request.method == 'POST':
        user_serializer = UserCreateSerializer(data=request.data)
        password = random_password()
        if user_serializer.is_valid():
            new_user = user_serializer.save()
            new_user.set_password(password)
            new_user.save()
            send_mail_registration.delay(
                msg=f"Здравствуйте, {request.data['name']} благодарим Вас зарегистрацию на сайте https://sadovodrynok.ru/. Доступы для входа на сайт: Логин:{request.data['email']}. Пароль: {password}",
                email=[user_serializer.validated_data['email']]
            )
            return Response(status=HTTP_201_CREATED)
        return Response({'status': 'email duplicate'}, status=HTTP_304_NOT_MODIFIED)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset(request):
    if request.method == 'POST':
        password = random_password()
        new_user = User.objects.get(email=request.data['email'])
        new_user.set_password(password)
        new_user.save()
        send_mail_password_reset.delay(
            msg=f"Здравствуйте, {request.data['name']} ваш новый пароль на сайте https://sadovodrynok.ru/ {password}.",
            email=[request.data['email']]
        )
        return Response(status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def password_change(request):
    if request.method == 'POST':
        new_user = User.objects.get(id=request.data['user'])
        new_user.set_password(request.data['password'])
        new_user.save()
        send_mail_password_change.delay(
            email=[new_user.email]
        )
        return Response(status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_info(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer_user = UserInfoSerializer(user, data=request.data)
        if serializer_user.is_valid():
            serializer_user.save()
            return Response(serializer_user.data)
        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)

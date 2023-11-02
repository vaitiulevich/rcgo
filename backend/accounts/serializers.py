from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'phone', 'father_name', 'country', 'region', 'city', 'address')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name')

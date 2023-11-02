from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import OrderSerializer

from .models import Orders


class OrdersCreate(generics.CreateAPIView):
    model = Orders
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

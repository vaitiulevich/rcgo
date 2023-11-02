from django.urls import path
from .views import OrdersCreate

urlpatterns = [
    path('order/', OrdersCreate.as_view())
]

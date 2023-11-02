from django.contrib import admin
from .models import Orders, Basket


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass

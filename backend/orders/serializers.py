from rest_framework import serializers
from .models import Orders, Basket
from products.models import Product


class BasketSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Basket
        fields = ['products', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    baskets = BasketSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['address', 'fio', 'index', 'phone', 'email', 'delivery', 'baskets', 'payment', 'comment']

    def create(self, validated_data):
        baskets_data = validated_data.pop('baskets')
        order = Orders.objects.create(**validated_data)
        for basket in baskets_data:
            Basket(order=order, products=basket.pop('products'), quantity=int(basket.pop('quantity'))).save()
        return order

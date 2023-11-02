from django.db import models
from products.models import Product


class Orders(models.Model):
    address = models.TextField(verbose_name='Адрес')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    index = models.CharField(max_length=50, verbose_name='Индекс', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Почта')
    delivery = models.CharField(max_length=150, verbose_name="Способ доставки")
    payment = models.CharField(max_length=150, verbose_name="Способ оплаты")
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Basket(models.Model):
    quantity = models.IntegerField(verbose_name="Кол-во")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукты')
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='baskets', verbose_name='Заказ')

    def __str__(self):
        return f"{self.products}<->{self.quantity}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'

from django.db import models
from django_resized import ResizedImageField
from categories.models import SubCategory


class Rates(models.Model):
    usd = models.FloatField(verbose_name='Цена с наценкой', default=3.15)
    rus = models.FloatField(verbose_name='Цена с наценкой', default=3.38)

    def __str__(self):
        return f"{self.rus}<->{self.usd}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы валют'


class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ссылка поставщика', db_index=True, unique=True)
    margin = models.IntegerField(verbose_name='Наценка', default=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.TextField(verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка на продукт')
    price_ru = models.FloatField(verbose_name='Цена в российских рублях', blank=True, null=True, )
    margin_price = models.FloatField(verbose_name='Цена с наценкой')
    price_usd = models.FloatField(verbose_name='Цена в долларах', blank=True, null=True, )
    dealer_price_ru = models.FloatField(verbose_name='Диллерская цена', blank=True, null=True, )
    description = models.TextField(verbose_name='Описание')
    article_sup = models.CharField(max_length=100, verbose_name='Артикул_поставщика')
    quantity_composition = models.CharField(max_length=100, verbose_name='Количество на складе')
    quantity = models.CharField(max_length=100, default='0', verbose_name='Количество у продавца')
    supp_link = models.TextField(verbose_name='Ссылка на товар у поставщика', blank=True, null=True, )
    brand = models.CharField(max_length=150, verbose_name='Изготовитель', blank=True, null=True, )
    category = models.ForeignKey(SubCategory, related_name="product", on_delete=models.CASCADE,
                                 verbose_name='Категория')
    characteristics = models.JSONField(blank=True, null=True, verbose_name='Характеристики')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class ProductImage(models.Model):
    img_low = ResizedImageField(upload_to='images/', size=[180, 120],
                                quality=100, crop=['middle', 'center'],
                                verbose_name='Картинка', force_format='JPEG', keep_meta=False)
    img_medium = ResizedImageField(upload_to='images/', size=[500, 330],
                                   quality=100, crop=['middle', 'center'],
                                   verbose_name='Картинка', force_format='JPEG', keep_meta=False)
    img_high = ResizedImageField(upload_to='images/', size=[720, 540],
                                 quality=100, crop=['middle', 'center'],
                                 verbose_name='Картинка', force_format='JPEG', keep_meta=False)
    image_url = models.TextField(verbose_name="Оригинальная ссылка")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Товар")

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Картинки товаров'


from django.db.models.signals import pre_save
from django.dispatch import receiver

# @receiver(pre_save, sender=ProductImage)
# def calc_ac_total(sender, instance, **kwargs):
#     os.remove(str(instance.img))

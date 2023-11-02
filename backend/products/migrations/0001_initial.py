# Generated by Django 4.2.4 on 2023-08-25 13:00

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка на продукт')),
                ('price_ru', models.FloatField(blank=True, null=True, verbose_name='Цена в российских рублях')),
                ('margin_price', models.FloatField(verbose_name='Цена с наценкой')),
                ('price_usd', models.FloatField(blank=True, null=True, verbose_name='Цена в долларах')),
                ('dealer_price_ru', models.FloatField(blank=True, null=True, verbose_name='Диллерская цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('article_sup', models.CharField(max_length=80, verbose_name='Артикул_поставщика')),
                ('quantity_composition', models.CharField(max_length=100, verbose_name='Количество на складе')),
                ('quantity', models.CharField(default='0', max_length=100, verbose_name='Количество у продавца')),
                ('supp_link', models.TextField(blank=True, null=True, verbose_name='Ссылка на товар у поставщика')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Изготовитель')),
                ('characteristics', models.JSONField(blank=True, null=True, verbose_name='Характеристики')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField(default=3.15, verbose_name='Цена с наценкой')),
                ('rus', models.FloatField(default=3.38, verbose_name='Цена с наценкой')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы валют',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Ссылка поставщика')),
                ('margin', models.IntegerField(default=30, verbose_name='Наценка')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, scale=None, size=[600, 800], upload_to='images/', verbose_name='Картинка')),
                ('image_url', models.TextField(verbose_name='Оригинальная ссылка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Картинки товаров',
            },
        ),
    ]
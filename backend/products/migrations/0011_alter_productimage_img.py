# Generated by Django 4.2.4 on 2023-09-03 21:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_productimage_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=100, scale=None, size=[1280, 1024], upload_to='images/', verbose_name='Картинка'),
        ),
    ]

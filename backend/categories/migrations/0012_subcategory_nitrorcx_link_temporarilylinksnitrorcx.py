# Generated by Django 4.2.4 on 2023-10-03 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_alter_subcategory_hobbycenter_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='nitrorcx_link',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на парсинг nitrorcx_link'),
        ),
        migrations.CreateModel(
            name='TemporarilyLinksNitrorcx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.JSONField(verbose_name='Промежуточные ссылки на парсинг')),
                ('date', models.DateField(auto_now_add=True, verbose_name='День временных ссылок')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Ссылка Nitrorcx',
                'verbose_name_plural': 'Промежуточные ссылки Nitrorcx',
            },
        ),
    ]

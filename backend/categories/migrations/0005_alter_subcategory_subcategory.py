# Generated by Django 4.2.4 on 2023-08-28 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_temporarilylinksbrrc_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='categories.category', verbose_name='Категория'),
        ),
    ]

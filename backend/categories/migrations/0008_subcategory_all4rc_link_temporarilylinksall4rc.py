# Generated by Django 4.2.4 on 2023-09-13 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_alter_temporarilylinksbrrc_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='all4rc_link',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на парсинг all4rc'),
        ),
        migrations.CreateModel(
            name='TemporarilyLinksAll4rc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.JSONField(verbose_name='Промежуточные ссылки на парсинг')),
                ('date', models.DateField(auto_now_add=True, verbose_name='День временных ссылок')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Ссылка All4rc',
                'verbose_name_plural': 'Промежуточная ссылки All4rc',
            },
        ),
    ]

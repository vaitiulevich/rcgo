from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True, verbose_name='Электронная почта')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия', null=True)
    father_name = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', null=True)
    country = models.CharField(max_length=50, verbose_name='Страна', null=True)
    region = models.CharField(max_length=50, verbose_name='Область', null=True)
    city = models.CharField(max_length=50, verbose_name='Населенный пункт', null=True)
    address = models.CharField(max_length=50, verbose_name='Адрес', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

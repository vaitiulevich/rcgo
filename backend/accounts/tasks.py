from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_mail_password_change(email):
    sleep(20)
    send_mail(subject='Восстановление пароля!',
              message="Вы успешно изменили пароль на сайте https://sadovodrynok.ru/.",
              from_email='officialsadovodrynok@gmail.com',
              recipient_list=email,
              fail_silently=True, )


@shared_task()
def send_mail_password_reset(email, msg):
    sleep(20)
    send_mail(subject='Восстановление пароля!',
              message=msg,
              from_email='officialsadovodrynok@gmail.com',
              recipient_list=email,
              fail_silently=True, )


@shared_task()
def send_mail_registration(email, msg):
    sleep(20)
    send_mail(subject='Успешная регистрация!',
              message=msg,
              from_email='officialsadovodrynok@gmail.com',
              recipient_list=email,
              fail_silently=True, )

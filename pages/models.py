from django.db import models


class Contact(models.Model):
    description = models.CharField(max_length=255, verbose_name='Описание')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='Электронная почта')

    def __str__(self):
        return self.city

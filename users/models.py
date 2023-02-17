from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождение', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='Почта', null=True, blank=True)
    drivers_licence = models.CharField(max_length=255, verbose_name='Права')
    drivers_licence_img = models.ImageField(upload_to='users/', default='default.png')
    drivers_series = models.CharField(max_length=255, verbose_name='Серия прав', null=True, blank=True)
    drivers_number = models.CharField(max_length=255, verbose_name='Номер прав', null=True, blank=True)
    experience = models.CharField(max_length=255, verbose_name='Стаж')
    passport_doled_out = models.DateField(verbose_name='Паспорт выдан', null=True, blank=True)
    passport_series = models.CharField(max_length=255, verbose_name='Серия паспорта', null=True, blank=True)
    passport_number = models.CharField(max_length=255, verbose_name='Номер паспорт', null=True, blank=True)
    passport_issued = models.CharField(max_length=255, verbose_name="Кем выдан", null=True, blank=True)
    passport_img = models.ImageField(upload_to='users/', default='default.png')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return f'{self.name} {self.phone}'

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
from users.models import Users
from reservations.models import Reserve
from charges.models import Income


class Agreement(models.Model):
    registration_date = models.DateField(auto_now=True)
    reserve_id = models.ForeignKey(Reserve, on_delete=models.DO_NOTHING)
    # service = models.ManyToManyField('Service', verbose_name='Услуги', null=True, blank=True,)
    total = models.IntegerField()
    total_summ = models.IntegerField()
    territory_of_use = models.CharField(max_length=255, verbose_name='Территория использования ТС', null=True, blank=True)

    def __str__(self):
        return f'{self.registration_date}'


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Service name")
    name_rus = models.CharField(max_length=255, verbose_name="Наименование услуги")
    description = models.CharField(max_length=255, verbose_name="Service description")
    description_rus = models.CharField(max_length=255, verbose_name="Описание услуги")
    price = models.IntegerField(verbose_name='Цена услуги')
    image = models.ImageField(verbose_name='Картинка услуги', upload_to='service/', default='default.png')

    def __str__(self):
        return f'{self.name}'


@receiver(pre_save, sender=Agreement)
def agreement_check(sender, instance, **kwargs):
    try:
        agreement_id = Agreement.objects.get(reserve_id=instance.reserve_id.id)
        income_id = Income.objects.get(income_reserve_id=agreement_id.reserve_id.id)
        agreement_id.delete()
        income_id.delete()
    except ObjectDoesNotExist:
        pass


@receiver(post_save, sender=Agreement)
def agreement_income_add(sender, created, instance, **kwargs):
    try:
        income_id = Income.objects.get(income_reserve_id=instance.reserve_id.id)
    except ObjectDoesNotExist:
        income = Income.objects.create(income_reserve_id=instance.reserve_id.id,
                                       car_income_id=instance.reserve_id.reserve_car, income_amount=instance.total_summ)
        income.save()

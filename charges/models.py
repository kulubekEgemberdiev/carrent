from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from _datetime import datetime

from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

import cars


class Income(models.Model):
    income_reserve_id = models.IntegerField()
    car_income_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE, verbose_name='ID Машины')
    income_amount = models.IntegerField(verbose_name='Сумма')
    order_date = models.DateTimeField(default=datetime.now, verbose_name="Дата")

    def __str__(self):
        return f'{self.car_income_id} | Cумма: {self.income_amount}'


class Outcome(models.Model):
    outcome_reserve_id = models.IntegerField(blank=True, null=True)
    outcome_remark = models.CharField(max_length=255, blank=True, null=True, verbose_name='Комментарии')
    car_outcome_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE, verbose_name='ID Машины')
    outcome_amount = models.IntegerField(verbose_name='Сумма')
    order_date = models.DateTimeField(default=datetime.now, verbose_name="Дата")

    def __str__(self):
        return f'{self.car_outcome_id} | Cумма: {self.outcome_amount}'


class Profit(models.Model):
    car_profit_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE, verbose_name='ID Машины')
    amount = models.IntegerField(verbose_name='Сумма', default=0)

    def __str__(self):
        return f'{self.car_profit_id} | Cумма: {self.amount}'


@receiver(post_save, sender=Income)
def car_income(sender, instance, created, **kwargs):
    if created:
        car = Profit.objects.get(car_profit_id=instance.car_income_id)
        car.amount = car.amount + instance.income_amount
        car.save()


@receiver(pre_save, sender=Income)
def car_income_change(sender, instance, **kwargs):
    try:
        income = Income.objects.get(id=instance.id)
        car = Profit.objects.get(car_profit_id=instance.car_income_id)
        car.amount = car.amount + instance.income_amount - income.income_amount
        car.save()
    except ObjectDoesNotExist:
        pass


@receiver(pre_delete, sender=Income)
def car_income_delete(sender, instance, **kwargs):
    income = Income.objects.get(id=instance.id)
    car = Profit.objects.get(car_profit_id=instance.car_income_id)
    car.amount = car.amount - income.income_amount
    car.save()


@receiver(post_save, sender=Outcome)
def car_outcome(sender, created, instance, **kwargs):
    if created:
        car = Profit.objects.get(car_profit_id=instance.car_outcome_id)
        car.amount = car.amount - instance.outcome_amount
        car.save()


@receiver(pre_save, sender=Outcome)
def car_outcome_change(sender, instance, **kwargs):
    try:
        outcome = Outcome.objects.get(id=instance.id)
        car = Profit.objects.get(car_profit_id=instance.car_outcome_id)
        car.amount = car.amount - instance.outcome_amount + outcome.outcome_amount
        car.save()
    except ObjectDoesNotExist:
        pass


@receiver(pre_delete, sender=Outcome)
def car_outcome_delete(sender, instance, **kwargs):
    outcome = Outcome.objects.get(id=instance.id)
    car = Profit.objects.get(car_profit_id=instance.car_outcome_id)
    car.amount = car.amount + outcome.outcome_amount
    car.save()

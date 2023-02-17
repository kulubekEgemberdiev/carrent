from django.core.exceptions import ObjectDoesNotExist
from django.db import models, IntegrityError
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from cars.models import Car
from _datetime import datetime

from charges.models import Income, Outcome
from users.models import Users

reserve_status = [
    ('Бронь', 'Бронь'),
    ('Выдана', 'Выдана'),
    ('Подтвержденная бронь', 'Подтвержденная бронь'),
    ('Тех Работы', 'Тех Работы'),
]
reserve_status_create = [
    ('Бронь', 'Бронь'),
    ('Подтвержденная бронь', 'Подтвержденная бронь'),
    ('Тех Работы', 'Тех Работы'),
]


class Reserve(models.Model):
    users = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True, blank=True)
    reserve_car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    reserve_car_js = models.CharField(max_length=255)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    registration_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=100, choices=reserve_status)
    outcome_res_amount = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    total_days = models.IntegerField(default=0, null=True, blank=True)
    total_summ = models.IntegerField(default=0, null=True, blank=True)
    change_summ = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.reserve_car} - {self.registration_date}'


@receiver(pre_save, sender=Reserve)
def car_total_days(sender, instance, **kwargs):
    car_js = instance.reserve_car.title.replace(" ", "")
    date_js = instance.departure_date.strftime("%d%m%Y")
    instance.reserve_car_js = car_js + date_js
    instance.total_days = (instance.arrival_date - instance.departure_date).days + 1
    if instance.total_days < 3:
        instance.total_summ = instance.total_days * instance.reserve_car.price_1_2
    elif 3 <= instance.total_days <= 7:
        instance.total_summ = instance.total_days * instance.reserve_car.price_3_7
    elif 8 <= instance.total_days <= 20:
        instance.total_summ = instance.total_days * instance.reserve_car.price_8_20
    elif 20 > instance.total_days:
        instance.total_summ = instance.total_days * instance.reserve_car.price_20


@receiver(post_save, sender=Reserve)
def car_status_check(sender, instance, **kwargs):
    # if instance.status == 'Выдана':
    #     try:
    #         income_check = Income.objects.get(income_reserve_id=instance.id)
    #         income_check.income_amount = instance.total_summ
    #         income_check.save()
    #     except ObjectDoesNotExist:
    #         income = Income.objects.create(car_income_id=instance.reserve_car, income_amount=instance.total_summ,
    #                                        income_reserve_id=instance.id)
    #         income.save()
    if instance.status == 'Тех Работы':
        try:
            outcome_check = Outcome.objects.get(outcome_reserve_id=instance.id)
            outcome_check.outcome_amount = instance.outcome_res_amount
            outcome_check.outcome_remark = instance.notes
            outcome_check.save()
        except ObjectDoesNotExist:
            outcome = Outcome.objects.create(car_outcome_id=instance.reserve_car,
                                             outcome_amount=instance.outcome_res_amount,
                                             outcome_remark=instance.notes,
                                             outcome_reserve_id=instance.id)
            outcome.save()


@receiver(post_delete, sender=Reserve)
def reservation_delete(sender, instance, **kwargs):
    if instance.status == 'Выдана':
        try:
            Income.objects.get(income_reserve_id=instance.id).delete()
        except ObjectDoesNotExist:
            pass
    elif instance.status == 'Тех Работы':
        try:
            Outcome.objects.get(outcome_reserve_id=instance.id).delete()
        except ObjectDoesNotExist:
            pass

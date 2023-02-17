from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from django.utils.translation import ugettext_lazy as _
from charges.models import Profit

CATEGORIES = [
    ('Эконом (класс B)', 'Эконом (класс B)'),
    ('Средний (класс C)', 'Средний (класс C)'),
    ('Бизнес (класс Е)', 'Бизнес (класс Е)'),
    ('Кроссовер (класс J)', 'Кроссовер (класс J)'),
]

GEAR_BOX = [
    ('Автомат', 'Автомат'),
    ('Механика', 'Механика'),
    ('Вариатор', 'Вариатор'),
]

FUEL_TYPE = [
    ('АИ-95', 'АИ-95'),
    ('АИ-92', 'АИ-92'),
    ('АИ-93', 'АИ-93'),
    ('АИ-80', 'АИ-80'),
    ('Дизель', 'Дизель'),
    ('Электро', 'Электро'),
]

CAR_BODY = [
    ('Хэтчбек', 'Хэтчбек'),
    ('Кроссовер', 'Кроссовер'),
    ('Седан', 'Седан'),
    ('Лифтбек', 'Лифтбек'),
    ('Внедорожник', 'Внедорожник'),
    ('Стретч', 'Стретч'),
    ('Купе', 'Купе'),
    ('Родстер', 'Родстер'),
    ('Кабриолет', 'Кабриолет'),
    ('Фургон', 'Фургон'),
    ('Минивэн', 'Минивэн'),
    ('Пикап', 'Пикап'),
    ('Тарга', 'Тарга'),
    ('Универсал', 'Универсал'),
]

WD = [
    ('Полный', 'Полный'),
    ('Передний', 'Передний'),
    ('Задний', 'Задний'),
]


class FunctionCar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Function Name')
    title_rus = models.CharField(max_length=255, verbose_name='Функции машины')

    def __str__(self):
        return f'{self.title}'


class Car(models.Model):
    car_owner = models.CharField(max_length=255, verbose_name='Собственник ТС')
    car_number = models.CharField(max_length=255, verbose_name='Номер машины')
    title = models.CharField(max_length=255, verbose_name='Название машины')
    description = models.TextField(verbose_name='Описание машины')
    car_price = models.IntegerField(verbose_name='Цена машины')
    description_rus = models.TextField(verbose_name='Описание машины')
    car_color = models.CharField(max_length=255, verbose_name='Car Color')
    car_color_rus = models.CharField(max_length=255, verbose_name='Цвет машины')
    car_class = models.CharField(max_length=255, choices=CATEGORIES, verbose_name='Класс машины')
    year = models.CharField(max_length=255, verbose_name='Год выпуска')
    engine_cap = models.CharField(max_length=255, verbose_name='Объем двигателя')
    engine_pow = models.CharField(max_length=255, verbose_name='Мощность двигателя')
    gear_box = models.CharField(max_length=255, choices=GEAR_BOX, verbose_name='Коробка передач')
    fuel_type = models.CharField(max_length=255, choices=FUEL_TYPE, verbose_name='Тип топлива')
    fuel_tank = models.CharField(max_length=255, verbose_name='Объекм бака')
    car_body = models.CharField(max_length=255, choices=CAR_BODY, verbose_name='Кузов машины')
    wd = models.CharField(max_length=255, choices=WD, verbose_name='Привод машины')
    mileage = models.CharField(max_length=255, verbose_name='Потребление топлива')
    vin = models.CharField(max_length=255, verbose_name='Идентификационный номер (VIN)')
    registration = models.CharField(max_length=255, verbose_name='Свидетельство о регистрации ТС')
    function_car = models.ManyToManyField(FunctionCar, verbose_name='Функции машины')
    price_1_2 = models.IntegerField(verbose_name='Цена от 1-2 дня')
    price_3_7 = models.IntegerField(verbose_name='Цена от 3-7 дней')
    price_8_20 = models.IntegerField(verbose_name='Цена от 8-20 дней')
    price_20 = models.IntegerField(verbose_name='Цена от 20 дней')
    image1 = models.ImageField(verbose_name='Картинка 1', upload_to='cars/', default='default.png')
    image2 = models.ImageField(verbose_name='Картинка 2', upload_to='cars/', null=True, blank=True)
    image3 = models.ImageField(verbose_name='Картинка 3', upload_to='cars/', null=True, blank=True)
    image4 = models.ImageField(verbose_name='Картинка 4', upload_to='cars/', null=True, blank=True)
    image5 = models.ImageField(verbose_name='Картинка 5', upload_to='cars/', null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.car_color})'


@receiver(post_save, sender=Car)
def car_profit(sender, instance, created, **kwargs):
    if created:
        Profit.objects.create(car_profit_id=instance, amount=0)

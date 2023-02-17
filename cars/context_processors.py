from .models import Car, FunctionCar


def cars(request):
    return {'cars': Car.objects.all()}


def func_car(request):
    return {'func_car': FunctionCar.objects.all()}


def car_b(request):
    return {'car_b': Car.objects.filter(car_class='Эконом (класс B)')}


def car_c(request):
    return {'car_c': Car.objects.filter(car_class='Средний (класс C)')}


def car_e(request):
    return {'car_e': Car.objects.filter(car_class='Бизнес (класс Е)')}


def car_j(request):
    return {'car_j': Car.objects.filter(car_class='Кроссовер (класс J)')}

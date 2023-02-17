from django import forms
from .models import Car, CATEGORIES, GEAR_BOX, FUEL_TYPE, CAR_BODY, WD


class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'car_owner', 'car_number', 'title', 'description', 'function_car', 'description_rus', 'car_color',
            'car_color_rus', 'car_class', 'year',
            'engine_cap', 'engine_pow', 'gear_box', 'fuel_type', 'fuel_tank', 'car_body', 'wd',
            'mileage', 'vin', 'registration', 'price_1_2', 'price_3_7', 'price_8_20', 'price_20',
            'image1', 'image2', 'image3', 'image4', 'image5')


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'car_owner', 'function_car', 'car_number', 'title', 'description', 'description_rus', 'car_color', 'car_color_rus',
            'car_class',
            'year',
            'engine_cap', 'engine_pow', 'gear_box', 'fuel_type', 'fuel_tank', 'car_body', 'wd',
            'mileage', 'vin', 'registration', 'price_1_2', 'price_3_7', 'price_8_20', 'price_20',
             'image1', 'image2', 'image3', 'image4', 'image5')

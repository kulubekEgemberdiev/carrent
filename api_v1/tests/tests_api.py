import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from cars.models import Car, FunctionCar
from agreement.models import Agreement, Service
from charges.models import Income, Outcome, Profit
from reservations.models import Reserve
from users.models import Users
from pages.models import Contact


class CarRentAPITest(APITestCase):
    def setUp(self):
        car_1 = Car.objects.create(
            car_owner='CityRent', car_number='01KG389FJT', title='Toyota Avencis',
            description='Description this car', car_price=12000, description_rus='Описание этой машины',
            car_color='Silver', car_color_rus='Серебристый', car_class=('Эконом (класс B)', 'Эконом (класс B)'),
            year=2009, engine_cap='2.2', engine_pow='150л/с', gear_box=('Автомат', 'Автомат'),
            fuel_type=('АИ-92', 'АИ-92'), fuel_tank='68', car_body=('Седан', 'Седан'), wd=('Передний', 'Передний'),
            mileage='14л/100км', vin='VIN94586312', registration='AUTO45687', price_1_2=10000, price_3_7=9500,
            price_8_20=9000, price_20=8000,
        )
        car_2 = Car.objects.create(
            car_owner='CityRent', car_number='04KG129FJT', title='Lamborghini Aventador',
            description='Description this car', car_price=2500000, description_rus='Описание этой машины',
            car_color='Orange', car_color_rus='Оранжевый', car_class=('Бизнес (класс Е)', 'Бизнес (класс Е)'),
            year=2023, engine_cap='4.0', engine_pow='480л/с', gear_box=('Автомат', 'Автомат'),
            fuel_type=('АИ-95', 'АИ-95'), fuel_tank='80', car_body=('Купе', 'Купе'), wd=('Полный', 'Полный'),
            mileage='19.6л/100км', vin='VIN94585958712', registration='AN784566992', price_1_2=120000, price_3_7=119000,
            price_8_20=118000, price_20=110000
        )
        func_1 = FunctionCar.objects.create(
            title='Heated all seats',
            title_rus='Подогрев всех сидений'
        )
        user = Users.objects.create(
            name='Карабек', second_name='Сарыбеков', last_name='Кызылтаевич', phone='+996(705)154879',
            drivers_licence='DL0052487', experience='4г.', address='г. Бишкек, ул. Фучика 47'

        )

        reserve = Reserve.objects.create(
            users=Users.objects.first(), reserve_car=Car.objects.first(), reserve_car_js='XZ chto eto',
            departure_date=datetime.date(2023, 2, 25), arrival_date=datetime.date(2023, 3, 25),
            status=('Бронь', 'Бронь'), outcome_res_amount=8000, notes='Запись в тестовую БД',
            total_days=30, total_summ=240000, change_summ=8000,
        )
        agreement = Agreement.objects.create(
            reserve_id=Reserve.objects.first(), total=8000, total_summ=240000, territory_of_use='г. Бишкек'
        )

        service = Service.objects.create(
            name='Car wash', name_rus='Автомойка', description='Free car wash for rented cars',
            description_rus='Бесплатная автомойка для арендованных автомобилей', price=0
        )

        income = Income.objects.create(income_reserve_id=1, car_income_id=Car.objects.first(), income_amount=145000)
        outcome = Outcome.objects.create(
            outcome_reserve_id=1, outcome_remark='Комментарий 1', car_outcome_id=Car.objects.first(),
            outcome_amount=100000,
        )

        profit = Profit.objects.create(car_profit_id=Car.objects.first(), amount=125000)
        contact = Contact.objects.create(
            description='Описание контакта', city='г. Бишкек', address='ул. Профсоюзная 25',
            phone='+996(555)444222', email='contact@mail.com',
        )
    def test_get_cars(self):
        url_cars = 'http://127.0.0.1:8000/api-v1/cars/'
        response = self.client.get(url_cars)
        print(f"Cars: \n{response.data}")

        url_funcs = 'http://127.0.0.1:8000/api-v1/car-functions/'
        response = self.client.get(url_funcs)
        print(f"Car functions: \n{response.data}")

    def test_get_agreements(self):
        agreement_url = 'http://127.0.0.1:8000/api-v1/agreements/'
        response = self.client.get(agreement_url)
        print(f"Agreements: \n{response.data}")

        service_url = 'http://127.0.0.1:8000/api-v1/service/'
        response = self.client.get(service_url)
        print(f"Services: \n{response.data}")

    def test_get_charges(self):
        income_url = 'http://127.0.0.1:8000/api-v1/income/'
        response = self.client.get(income_url)
        print(f"Income: \n{response.data}")

        outcome_url = 'http://127.0.0.1:8000/api-v1/outcome/'
        response = self.client.get(outcome_url)
        print(f"Outcome: \n{response.data}")

        profit_url = 'http://127.0.0.1:8000/api-v1/profit/'
        response = self.client.get(profit_url)
        print(f"Profit: \n{response.data}")

    def test_get_pages(self):
        contacts_url = 'http://127.0.0.1:8000/api-v1/contacts/'
        response = self.client.get(contacts_url)
        print(f"Contacts: \n{response.data}")

    def test_get_reservations(self):
        reserve_url = 'http://127.0.0.1:8000/api-v1/reserve/'
        response = self.client.get(reserve_url)
        print(f"Reserve: \n{response.data}")

    def test_get_users(self):
        users_url = 'http://127.0.0.1:8000/api-v1/users/'
        response = self.client.get(users_url)
        print(f"Users: \n{response.data}")

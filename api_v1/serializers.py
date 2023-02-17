from rest_framework import serializers

from agreement.models import Agreement, Service
from cars.models import Car, FunctionCar
from charges.models import Income, Outcome, Profit
from pages.models import Contact
from reservations.models import Reserve
from users.models import Users


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class FunctionCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionCar
        fields = "__all__"


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = "__all__"


class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

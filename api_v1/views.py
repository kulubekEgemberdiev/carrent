from rest_framework import viewsets

from api_v1.serializers import *
from cars.models import Car, FunctionCar
from agreement.models import Agreement, Service
from charges.models import Income, Outcome, Profit
from pages.models import Contact
from reservations.models import Reserve
from users.models import Users


# Create your views here.

# CARS
class CarsViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer


class CarFunctionsViewSet(viewsets.ModelViewSet):
    queryset = FunctionCar.objects.all()
    serializer_class = FunctionCarSerializer


# AGREEMENT
class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# CHARGES
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer


class ProfitViewSet(viewsets.ModelViewSet):
    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer


# PAGES
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# RESERVATION
class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer


# USERS
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

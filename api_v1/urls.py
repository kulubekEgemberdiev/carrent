from django.urls import path, include
from rest_framework import routers
from api_v1.views import *

router = routers.SimpleRouter()
# CARS
router.register(r'cars', CarsViewSet)
router.register(r'car-functions', CarFunctionsViewSet)
# AGREEMENT
router.register(r'agreements', AgreementViewSet)
router.register(r'service', ServiceViewSet)
# CHARGES
router.register(r'income', IncomeViewSet)
router.register(r'outcome', OutcomeViewSet)
router.register(r'profit', ProfitViewSet)
# PAGES
router.register(r'contacts', ContactsViewSet)
# RESERVATIONS
router.register(r'reserve', ReserveViewSet)
# USERS
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

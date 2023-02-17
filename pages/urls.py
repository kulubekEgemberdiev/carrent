from django.urls import path
from .views import (HomePageView, ContactPageView, ConditionsPageView, PricePageView, ServicePageView, ManagerPageView,
                    CarManagerPageView, ServiceManagerView, ServiceCreateView, ServiceDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contact'),
    path('conditions/', ConditionsPageView.as_view(), name='condition'),
    path('price/', PricePageView.as_view(), name='price'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('abai/', ManagerPageView.as_view(), name='manager_list'),
    path('manager/cars/', CarManagerPageView.as_view(), name='car_manager'),
    path('manager/service', ServiceManagerView.as_view(), name='service_manager'),
    path('manager/service/create', ServiceCreateView.as_view(), name='service_create'),
    path('manager/service/<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),
]

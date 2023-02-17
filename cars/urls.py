from django.urls import path
from .views import CarsListView, CategoryBListView, CategoryCListView, CategoryEListView, CategoryJListView, \
    CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, FunctionListView, FunctionDeleteView, FunctionCreateView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
    path('class_b/', CategoryBListView.as_view(), name='class_b'),
    path('class_c/', CategoryCListView.as_view(), name='class_c'),
    path('class_e/', CategoryEListView.as_view(), name='class_e'),
    path('class_j/', CategoryJListView.as_view(), name='class_j'),
    path('func_list/', FunctionListView.as_view(), name='func_list'),
    path('func_delete/<int:pk>/', FunctionDeleteView.as_view(), name='func_delete'),
    path('func_create/', FunctionCreateView.as_view(), name='func_create'),
]

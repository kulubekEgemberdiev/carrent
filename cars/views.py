from django.urls import reverse_lazy
from .models import Car, FunctionCar
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import CarCreateForm, CarUpdateForm


class CarsListView(ListView):
    model = Car
    template_name = 'cars/cars_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car_create.html'
    success_url = reverse_lazy('car_manager')
    fields = '__all__'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/car_update.html'
    success_url = reverse_lazy('car_manager')
    fields = '__all__'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('car_manager')


class CategoryBListView(ListView):
    model = Car
    template_name = 'cars/class_b.html'
    queryset = Car.objects.filter(car_class='Эконом (класс B)')


class CategoryCListView(ListView):
    model = Car
    template_name = 'cars/class_c.html'
    queryset = Car.objects.filter(car_class='Средний (класс C)')


class CategoryEListView(ListView):
    model = Car
    template_name = 'cars/class_e.html'
    queryset = Car.objects.filter(car_class='Бизнес (класс Е)')


class CategoryJListView(ListView):
    model = Car
    template_name = 'cars/class_j.html'
    queryset = Car.objects.filter(car_class='Кроссовер (класс J)')


class FunctionListView(ListView):
    model = FunctionCar
    template_name = 'manager/function_manager.html'


class FunctionDeleteView(DeleteView):
    model = FunctionCar
    template_name = 'cars/func_delete.html'
    success_url = reverse_lazy('func_list')


class FunctionCreateView(CreateView):
    model = FunctionCar
    template_name = 'cars/func_create.html'
    fields = '__all__'
    success_url = reverse_lazy('func_list')

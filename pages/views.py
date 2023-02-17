from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from agreement.models import Service
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail


class HomeSendFormEmail(View):

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        phone = request.GET.get('phone', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)
        reception_email = 'cityrent.kg@gmail.com'

        # Send Email
        send_mail(
            'City Rent email from site',
            f"Name: {name} \nphone: {phone} \nEmail: {email} \n Message: {message}",
            'cityrent.kg@gmail.com',  # Admin
            [
                reception_email
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.',))
        return redirect('home')


class SendFormEmail(View):

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        phone = request.GET.get('phone', None)
        email = request.GET.get('email', None)
        car = request.GET.get('car', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        reception_email = 'cityrent.kg@gmail.com'

        # Send Email
        send_mail(
            'City Rent email from car reservation',
            f"Name: {name} \nphone: {phone} \nEmail: {email} \nCar: {car} \n Start Date: {start_date} \n /"
            f"End Date: {end_date}",
            'cityrent.kg@gmail.com',  # Admin
            [
                reception_email
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.',))
        return redirect('home')


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class ConditionsPageView(TemplateView):
    template_name = 'pages/conditions.html'


class PricePageView(TemplateView):
    template_name = 'pages/price.html'


class ServicePageView(TemplateView):
    template_name = 'pages/service.html'


class ServiceManagerView(TemplateView):
    template_name = 'manager/service_manager.html'


class ServiceCreateView(UserPassesTestMixin, CreateView):
    model = Service
    template_name = 'manager/service_create.html'
    fields = '__all__'
    success_url = reverse_lazy('service_manager')

    def test_func(self):
        return self.request.user.is_staff


class ServiceDeleteView(UserPassesTestMixin, DeleteView):
    model = Service
    template_name = 'manager/service_delete.html'
    success_url = reverse_lazy('service_manager')

    def test_func(self):
        return self.request.user.is_staff


class ContactPageView(ListView):
    model = Contact
    template_name = 'pages/contact.html'


class ManagerPageView(UserPassesTestMixin, TemplateView):
    template_name = 'manager/manager_list.html'

    def test_func(self):
        return self.request.user.is_staff


class CarManagerPageView(UserPassesTestMixin, TemplateView):
    template_name = 'manager/car_manager.html'

    def test_func(self):
        return self.request.user.is_staff


def my_404(request, exception):
    return render(request, 'pages/error-404.html', locals())

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import ReserveCreateForm, ReserveUpdateForm
import reservations
from reservations.models import Reserve


class ReserveCreateView(CreateView):
    model = Reserve
    template_name = 'reservations/reserve_create.html'
    success_url = reverse_lazy('reserve_list')
    form_class = ReserveCreateForm


class ReserveListView(ListView):
    model = Reserve
    template_name = 'reservations/index.html'


class ReserveUpdateView(UpdateView):
    model = Reserve
    template_name = 'reservations/reserve_update.html'
    form_class = ReserveUpdateForm

    def get_success_url(self):
        if self.object.status == 'Бронь' or self.object.status == 'Тех Работы':
            return reverse('reserve_list')
        elif self.object.status == 'Выдана':
            return reverse('agreement_create', kwargs={'reserve_id': self.object.pk})


class ReserveDetailView(DetailView):
    model = Reserve
    template_name = 'reservations/reserve_detail.html'

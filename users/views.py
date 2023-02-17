from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Users
from .forms import UserCreateForm, UserUpdateForm


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'


class UserDetailView(DetailView):
    model = Users
    template_name = 'users/user_detail.html'


class UserCreateView(CreateView):
    model = Users
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('users_list')
    form_class = UserCreateForm


class UserUpdateView(UpdateView):
    model = Users
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users_list')
    form_class = UserUpdateForm


class UserDeleteView(DeleteView):
    model = Users
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users_list')

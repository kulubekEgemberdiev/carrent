from django import forms
from .models import Reserve, reserve_status, reserve_status_create
from cars.models import Car
from users.models import Users


class ReserveCreateForm(forms.ModelForm):
    users = forms.ModelChoiceField(label=False, queryset=Users.objects.all(), empty_label="Выберите клиента",
                                   required=False,
                                   widget=forms.Select(attrs={'class': 'form-control client-choose'}))
    reserve_car = forms.ModelChoiceField(label=False, queryset=Car.objects.all(),
                                         empty_label="Выберите машину", required=True,
                                         widget=forms.Select(attrs={'class': 'form-control reserve-car-title reserve-section-car-title'}))
    departure_date = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control ', 'id': 'id_departure_date'}),
                                     input_formats=('%d.%m.%Y',))
    arrival_date = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'id': 'id_arrival_date'}),
                                     input_formats=('%d.%m.%Y',))
    status = forms.ChoiceField(choices=reserve_status_create, label='Выберите статус', required=True, widget=forms.Select(
        attrs={'class': 'form-control'}))
    outcome_res_amount = forms.IntegerField(label='Расход', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(label='Заметки', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Reserve
        fields = ['users', 'reserve_car', 'departure_date', 'arrival_date', 'status', 'outcome_res_amount', 'notes']


class ReserveUpdateForm(forms.ModelForm):
    users = forms.ModelChoiceField(queryset=Users.objects.all(), empty_label="Выберите клиента",
                                   required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    reserve_car = forms.ModelChoiceField(queryset=Car.objects.all(), label=False,
                                         empty_label="Выберите машину", required=True,
                                         widget=forms.Select(attrs={'class': 'form-control reserve-car-title reserve-section-car-title'}))
    departure_date = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'id': 'id_departure_date'}),
                                     input_formats=('%d.%m.%Y',))
    arrival_date = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'id': 'id_arrival_date'}),
                                   input_formats=('%d.%m.%Y',))
    status = forms.ChoiceField(choices=reserve_status, label='Выбреите статус', required=True, widget=forms.Select(
        attrs={'class': 'form-control'}))
    outcome_res_amount = forms.IntegerField(label='Расход', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    notes = forms.CharField(label='Заметки', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Reserve
        fields = ['users', 'reserve_car', 'departure_date', 'arrival_date', 'status', 'outcome_res_amount', 'notes']

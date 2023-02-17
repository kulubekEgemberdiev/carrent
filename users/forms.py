from django import forms
from .models import Users


class UserCreateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_name = forms.CharField(label='Фамилия', required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Отчество', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.CharField(label='День рождения', required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone = forms.CharField(label='Телефон', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Почта', required=False,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    drivers_licence = forms.CharField(label='Права', required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    drivers_licence_img = forms.ImageField(label='Фото прав', required=False,
                                           widget=forms.FileInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(label='Стаж вождения', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_img = forms.ImageField(label='Фото пасспорта', required=False,
                                    widget=forms.FileInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_doled_out = forms.CharField(label='Паспорт выдан', required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Users
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_name = forms.CharField(label='Фамилия', required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Отчество', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.CharField(label='День рождения', required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Почта', required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    drivers_licence = forms.CharField(label='Права', required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    drivers_licence_img = forms.ImageField(label='Фото прав', required=False,
                                           widget=forms.FileInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(label='Стаж вождения', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_img = forms.ImageField(label='Фото пасспорта', required=False,
                                    widget=forms.FileInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    passport_doled_out = forms.CharField(label='Паспорт выдан', required=True,
                                         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Users
        fields = '__all__'

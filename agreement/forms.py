from django import forms

from agreement.models import Agreement


class AgreementCreateForm(forms.ModelForm):
    territory_of_use = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'г. Бишкек'}))

    class Meta:
        model = Agreement
        fields = '__all__'

from django import forms
from charges.models import Income, Outcome


class IncomeForm(forms.ModelForm):
    model = Income
    fields = "__all__"

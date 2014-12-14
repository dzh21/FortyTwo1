# -*- coding: utf-8 -*-
from django.forms import ModelForm
from tasks42.models import Person
from tasks42.widgets import DatePickerInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        labels = {
            'surname': 'Last name'
        }
        widgets = {
            'date_of_birth': DatePickerInput(attrs={'class': 'form-control'})
        }

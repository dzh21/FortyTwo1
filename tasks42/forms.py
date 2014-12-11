# -*- coding: utf-8 -*-
from django.forms import ModelForm
from tasks42.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        labels = {
            'surname': 'Last name'
        }


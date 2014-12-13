# -*- coding: utf-8 -*-
from django.forms import ModelForm
from tasks42.models import Person
from django.forms.extras.widgets import SelectDateWidget


class PersonForm(ModelForm):
    class Meta:
        model = Person
        labels = {
            'surname': 'Last name'
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'datepicker'
        })
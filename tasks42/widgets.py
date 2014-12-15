# -*- coding: utf-8 -*-
from django.forms.widgets import TextInput


class DatePickerInput(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'datepicker'}
        if attrs is not None:
            if 'class' in attrs.keys():
                default_attrs['class'] += " " + attrs['class']
                attrs.pop('class')
            default_attrs.update(attrs)
        super(DatePickerInput, self).__init__(default_attrs)

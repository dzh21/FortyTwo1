# -*- coding: utf-8 -*-
from django.conf import settings


def add_settings_to_context(request):
    return {'settings': settings}

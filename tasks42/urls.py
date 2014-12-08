# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from tasks42 import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index),
)

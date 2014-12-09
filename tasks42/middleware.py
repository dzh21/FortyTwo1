# -*- coding: utf-8 -*-
from tasks42.models import RequestObject
from django.utils import timezone


class SaveHttpRequest(object):
    def process_request(self, request):
        req = RequestObject()
        req.desc = request
        req.remote_address = request.META['REMOTE_ADDR']
        req.event_date_time = timezone.now()
        req.save()
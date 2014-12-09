from django.contrib import admin
from tasks42.models import Person, RequestObject

admin.site.register(Person)


class RequestObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_date_time', 'remote_address', )

admin.site.register(RequestObject, RequestObjectAdmin)
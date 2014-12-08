from django.shortcuts import render
from tasks42.models import Person


def index(request):
    return render(request, "home.html", {'persons': Person.objects.all()})

from django.shortcuts import render
from tasks42.models import Person


def index(request):
    return render(request, "home.html", {'persons': Person.objects.all()})


def requests(request):
    return render(request, "requests.html", {'response': ''})

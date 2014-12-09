from django.shortcuts import render
from tasks42.models import Person, RequestObject


def index(request):
    return render(request, "home.html", {'persons': Person.objects.all()})


def requests(request):
    return render(request, "requests.html", {'requests': RequestObject.objects.all()})

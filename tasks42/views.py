from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks42.models import Person, RequestObject
from tasks42.forms import PersonForm


def index(request):
    return render(request, "home.html", {'persons': Person.objects.all()})


def requests(request):
    return render(
        request,
        "requests.html",
        {'requests': list(RequestObject.objects.order_by('event_date_time'))[:10]}
    )


def edit_contacts(request):
    person = Person.objects.get(pk=1)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)

    return render(request, "edit_contacts.html", {'edit_person_form': form})

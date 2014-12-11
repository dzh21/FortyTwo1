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
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            saved_person = form.save()
            if saved_person.photo:
                resize_photo(saved_person.photo)
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)

    return render(request, "edit_contacts.html", {'edit_person_form': form})


def resize_photo(img):
    """ resize uploaded photo to 200x200 """
    from PIL import Image
    from django.conf import settings

    image = Image.open(settings.MEDIA_ROOT + '/' + str(img))
    image.thumbnail((200, 200), Image.ANTIALIAS)
    image.save(settings.MEDIA_ROOT + '/' + str(img), "JPEG")
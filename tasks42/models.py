from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField()
    photo = models.FileField(upload_to='photos', blank=True)

    def __unicode__(self):
        return self.name + ' ' + self.surname


class RequestObject(models.Model):
    desc = models.TextField()
    remote_address = models.CharField(max_length=20, default='localhost')
    event_date_time = models.DateTimeField()

    def __unicode__(self):
        return "Request #" + str(self.id)


class OperationOnModels(models.Model):
    date_time = models.DateTimeField(default=timezone.now())
    operation = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)


def signal_save_update_callback(sender, **kwargs):
    if sender.__name__ != 'OperationOnModels':
        op = OperationOnModels()
        op.operation = kwargs['created'] and 'create' or 'edit'
        op.model_name = sender.__name__
        op.save()

post_save.connect(signal_save_update_callback)
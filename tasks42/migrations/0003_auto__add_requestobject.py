# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestObject'
        db.create_table(u'tasks42_requestobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('remote_address', self.gf('django.db.models.fields.CharField')(default='localhost', max_length=20)),
            ('event_date_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'tasks42', ['RequestObject'])


    def backwards(self, orm):
        # Deleting model 'RequestObject'
        db.delete_table(u'tasks42_requestobject')


    models = {
        u'tasks42.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tasks42.requestobject': {
            'Meta': {'object_name': 'RequestObject'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'event_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_address': ('django.db.models.fields.CharField', [], {'default': "'localhost'", 'max_length': '20'})
        }
    }

    complete_apps = ['tasks42']
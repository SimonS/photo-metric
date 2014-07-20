# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Checkin'
        db.create_table('checkins_checkin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('checkins', ['Checkin'])


    def backwards(self, orm):
        # Deleting model 'Checkin'
        db.delete_table('checkins_checkin')


    models = {
        'checkins.checkin': {
            'Meta': {'object_name': 'Checkin'},
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['checkins']
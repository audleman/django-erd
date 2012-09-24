# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelRenderSettings'
        db.create_table(u'django_erd_modelrendersettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('selected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('top', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('left', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('z', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'django_erd', ['ModelRenderSettings'])


    def backwards(self, orm):
        # Deleting model 'ModelRenderSettings'
        db.delete_table(u'django_erd_modelrendersettings')


    models = {
        u'django_erd.modelrendersettings': {
            'Meta': {'object_name': 'ModelRenderSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'top': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'z': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['django_erd']
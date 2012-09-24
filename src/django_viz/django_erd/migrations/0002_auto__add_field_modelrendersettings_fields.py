# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ModelRenderSettings.fields'
        db.add_column(u'django_erd_modelrendersettings', 'fields',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2000, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ModelRenderSettings.fields'
        db.delete_column(u'django_erd_modelrendersettings', 'fields')


    models = {
        u'django_erd.modelrendersettings': {
            'Meta': {'object_name': 'ModelRenderSettings'},
            'fields': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'top': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'z': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['django_erd']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.created'
        db.alter_column(u'milcam_photo', 'created', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Photo.created'
        db.alter_column(u'milcam_photo', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        'milcam.device': {
            'Meta': {'object_name': 'Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        'milcam.photo': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'db_index': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['milcam.Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'position': ('geoposition.fields.GeopositionField', [], {'max_length': '42'})
        }
    }

    complete_apps = ['milcam']
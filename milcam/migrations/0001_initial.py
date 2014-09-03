# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table(u'milcam_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
        ))
        db.send_create_signal(u'milcam', ['Device'])

        # Adding model 'Photo'
        db.create_table(u'milcam_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['milcam.Device'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 1, 0, 0), auto_now_add=True, db_index=True, blank=True)),
            ('position', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
        ))
        db.send_create_signal(u'milcam', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table(u'milcam_device')

        # Deleting model 'Photo'
        db.delete_table(u'milcam_photo')


    models = {
        u'milcam.device': {
            'Meta': {'object_name': 'Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'milcam.photo': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 1, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['milcam.Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'position': ('geoposition.fields.GeopositionField', [], {'max_length': '42'})
        }
    }

    complete_apps = ['milcam']
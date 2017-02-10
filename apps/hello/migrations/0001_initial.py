# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'hello_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_birth', self.gf('django.db.models.fields.DateField')(null=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'hello_contact')


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['hello']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'gadb_action'
        db.create_table(u'myapp_gadb_action', (
            ('action_id', self.gf('django.db.models.fields.IntegerField')(max_length=4, primary_key=True)),
            ('bill_id', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('datetime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('chamber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('motion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rcs_num', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('aye', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('not_voting', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('exc_abs', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('exc_vote', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('total_votes', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['gadb_action'])

        # Adding model 'gadb_bill'
        db.create_table(u'myapp_gadb_bill', (
            ('bill_id', self.gf('django.db.models.fields.IntegerField')(max_length=4, primary_key=True)),
            ('chamber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('doc_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('doc_url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_featured', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_action', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['gadb_bill'])

        # Adding model 'gadb_legislator'
        db.create_table(u'myapp_gadb_legislator', (
            ('legislator_id', self.gf('django.db.models.fields.IntegerField')(max_length=11, primary_key=True)),
            ('ncga_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('first_name', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('chamber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('district', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('party', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('office_addr', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('legislative_addr', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('terms', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('counties', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('home_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_votes', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('eligible_votes', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('actual_votes', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('with_majority', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('against_majority', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['gadb_legislator'])

        # Adding model 'gadb_stats'
        db.create_table(u'myapp_gadb_stats', (
            ('stat_id', self.gf('django.db.models.fields.IntegerField')(max_length=11, primary_key=True)),
            ('stat_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['gadb_stats'])

        # Adding model 'gadb_vote'
        db.create_table(u'myapp_gadb_vote', (
            ('vote_id', self.gf('django.db.models.fields.IntegerField')(max_length=11, primary_key=True)),
            ('legislator_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('action_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('vote', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('with_party', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal(u'myapp', ['gadb_vote'])


    def backwards(self, orm):
        # Deleting model 'gadb_action'
        db.delete_table(u'myapp_gadb_action')

        # Deleting model 'gadb_bill'
        db.delete_table(u'myapp_gadb_bill')

        # Deleting model 'gadb_legislator'
        db.delete_table(u'myapp_gadb_legislator')

        # Deleting model 'gadb_stats'
        db.delete_table(u'myapp_gadb_stats')

        # Deleting model 'gadb_vote'
        db.delete_table(u'myapp_gadb_vote')


    models = {
        u'myapp.gadb_action': {
            'Meta': {'object_name': 'gadb_action'},
            'action_id': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'primary_key': 'True'}),
            'aye': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bill_id': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'chamber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'datetime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'exc_abs': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'exc_vote': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'motion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'not_voting': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'rcs_num': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_votes': ('django.db.models.fields.IntegerField', [], {'max_length': '12'})
        },
        u'myapp.gadb_bill': {
            'Meta': {'object_name': 'gadb_bill'},
            'bill_id': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'primary_key': 'True'}),
            'chamber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'doc_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'doc_url': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'is_featured': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'last_action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.gadb_legislator': {
            'Meta': {'object_name': 'gadb_legislator'},
            'actual_votes': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'against_majority': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'chamber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'counties': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'district': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'eligible_votes': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'home_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'legislative_addr': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'legislator_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'primary_key': 'True'}),
            'ncga_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'office_addr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'terms': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_votes': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'with_majority': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        u'myapp.gadb_stats': {
            'Meta': {'object_name': 'gadb_stats'},
            'stat_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'primary_key': 'True'}),
            'stat_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.gadb_vote': {
            'Meta': {'object_name': 'gadb_vote'},
            'action_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'legislator_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'vote_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'primary_key': 'True'}),
            'with_party': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['myapp']
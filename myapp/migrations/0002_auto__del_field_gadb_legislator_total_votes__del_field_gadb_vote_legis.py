# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'gadb_legislator.total_votes'
        db.delete_column(u'myapp_gadb_legislator', 'total_votes')

        # Adding M2M table for field votelist on 'gadb_legislator'
        m2m_table_name = db.shorten_name(u'myapp_gadb_legislator_votelist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gadb_legislator', models.ForeignKey(orm[u'myapp.gadb_legislator'], null=False)),
            ('gadb_vote', models.ForeignKey(orm[u'myapp.gadb_vote'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gadb_legislator_id', 'gadb_vote_id'])

        # Deleting field 'gadb_vote.legislator_id'
        db.delete_column(u'myapp_gadb_vote', 'legislator_id')


    def backwards(self, orm):
        # Adding field 'gadb_legislator.total_votes'
        db.add_column(u'myapp_gadb_legislator', 'total_votes',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11),
                      keep_default=False)

        # Removing M2M table for field votelist on 'gadb_legislator'
        db.delete_table(db.shorten_name(u'myapp_gadb_legislator_votelist'))

        # Adding field 'gadb_vote.legislator_id'
        db.add_column(u'myapp_gadb_vote', 'legislator_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11),
                      keep_default=False)


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
            'votelist': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.gadb_vote']", 'symmetrical': 'False'}),
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
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'vote_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'primary_key': 'True'}),
            'with_party': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['myapp']
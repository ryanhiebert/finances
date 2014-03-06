# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entry.payee'
        db.delete_column('finances_entry', 'payee')

        # Adding field 'Entry.memo'
        db.add_column('finances_entry', 'memo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.date'
        db.add_column('finances_transaction', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 6, 0, 0)),
                      keep_default=False)

        # Adding field 'Transaction.payee'
        db.add_column('finances_transaction', 'payee',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.memo'
        db.add_column('finances_transaction', 'memo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Entry.payee'
        db.add_column('finances_entry', 'payee',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Entry.memo'
        db.delete_column('finances_entry', 'memo')

        # Deleting field 'Transaction.date'
        db.delete_column('finances_transaction', 'date')

        # Deleting field 'Transaction.payee'
        db.delete_column('finances_transaction', 'payee')

        # Deleting field 'Transaction.memo'
        db.delete_column('finances_transaction', 'memo')


    models = {
        'finances.account': {
            'Meta': {'unique_together': "(('journal', 'name'),)", 'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts'", 'to': "orm['finances.Journal']"}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'finances.allotment': {
            'Meta': {'unique_together': "(('category', 'budget'),)", 'object_name': 'Allotment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '32', 'decimal_places': '2'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allotments'", 'to': "orm['finances.Budget']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allotments'", 'to': "orm['finances.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'finances.budget': {
            'Meta': {'object_name': 'Budget'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'categories'", 'to': "orm['finances.Category']", 'through': "orm['finances.Allotment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'budgets'", 'to': "orm['finances.Journal']"}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'stop': ('django.db.models.fields.DateField', [], {})
        },
        'finances.category': {
            'Meta': {'unique_together': "(('journal', 'name'),)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finances.Journal']"}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'finances.entry': {
            'Meta': {'object_name': 'Entry'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['finances.Account']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '32', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['finances.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['finances.Transaction']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'finances.journal': {
            'Meta': {'object_name': 'Journal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'finances.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'payee': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['finances']
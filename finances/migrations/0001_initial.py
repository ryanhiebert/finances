# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journal'
        db.create_table('finances_journal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('finances', ['Journal'])

        # Adding model 'Category'
        db.create_table('finances_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Journal'])),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('finances', ['Category'])

        # Adding unique constraint on 'Category', fields ['journal', 'name']
        db.create_unique('finances_category', ['journal_id', 'name'])

        # Adding model 'Budget'
        db.create_table('finances_budget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='budgets', to=orm['finances.Journal'])),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('stop', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('finances', ['Budget'])

        # Adding model 'Allotment'
        db.create_table('finances_allotment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allotments', to=orm['finances.Category'])),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allotments', to=orm['finances.Budget'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=32, decimal_places=2)),
        ))
        db.send_create_signal('finances', ['Allotment'])

        # Adding unique constraint on 'Allotment', fields ['category', 'budget']
        db.create_unique('finances_allotment', ['category_id', 'budget_id'])

        # Adding model 'Account'
        db.create_table('finances_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accounts', to=orm['finances.Journal'])),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('finances', ['Account'])

        # Adding unique constraint on 'Account', fields ['journal', 'name']
        db.create_unique('finances_account', ['journal_id', 'name'])

        # Adding model 'Transaction'
        db.create_table('finances_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('finances', ['Transaction'])

        # Adding model 'Entry'
        db.create_table('finances_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['finances.Transaction'])),
            ('payee', self.gf('django.db.models.fields.CharField')(blank=True, max_length=256, null=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['finances.Account'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['finances.Category'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=32, decimal_places=2)),
        ))
        db.send_create_signal('finances', ['Entry'])


    def backwards(self, orm):
        # Removing unique constraint on 'Account', fields ['journal', 'name']
        db.delete_unique('finances_account', ['journal_id', 'name'])

        # Removing unique constraint on 'Allotment', fields ['category', 'budget']
        db.delete_unique('finances_allotment', ['category_id', 'budget_id'])

        # Removing unique constraint on 'Category', fields ['journal', 'name']
        db.delete_unique('finances_category', ['journal_id', 'name'])

        # Deleting model 'Journal'
        db.delete_table('finances_journal')

        # Deleting model 'Category'
        db.delete_table('finances_category')

        # Deleting model 'Budget'
        db.delete_table('finances_budget')

        # Deleting model 'Allotment'
        db.delete_table('finances_allotment')

        # Deleting model 'Account'
        db.delete_table('finances_account')

        # Deleting model 'Transaction'
        db.delete_table('finances_transaction')

        # Deleting model 'Entry'
        db.delete_table('finances_entry')


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
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categories'", 'to': "orm['finances.Category']", 'symmetrical': 'False', 'through': "orm['finances.Allotment']"}),
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
            'payee': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256', 'null': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['finances.Transaction']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'finances.journal': {
            'Meta': {'object_name': 'Journal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'finances.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['finances']
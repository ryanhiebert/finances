from django.db import models

class Journal(models.Model):
    class Meta:
        unique_together = (('parent', 'name'),)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    name = models.SlugField()

class Category(models.Model):
    class Meta:
        unique_together = (('journal', 'parent', 'name'),)
    journal = models.ForeignKey(Journal)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    name = models.SlugField()

class Budget(models.Model):
    class Meta:
        unique_together = (('journal', 'previous', 'name'),)
    journal = models.ForeignKey(Journal, related_name='budgets')
    name = models.CharField(max_length=256)
    previous = models.OneToOneField('self', related_name='next')
    start = models.DateField()
    stop = models.DateField()
    categories = models.ManyToManyField(Category, through='Allotment', related_name='budgets')

class Allotment(models.Model):
    class Meta:
        unique_together = (('category', 'budget'),)
    category = models.ForeignKey(Category, related_name='allotments')
    budget = models.ForeignKey(Budget, related_name='allotments')
    amount = models.DecimalField(max_digits=32, decimal_places=2)

class Account(models.Model):
    journals = models.ManyToManyField(Journal, related_name='accounts')
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    name = models.SlugField()
    type = models.CharField(max_length=2) # 'Dr' or 'Cr'

class Transaction(models.Model):
    number = models.CharField(max_length=256)
    date = models.DateField()
    payee = models.CharField(max_length=256, null=True, blank=True)
    memo = models.CharField(max_length=256, default='', blank=True)

class Entry(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='entries')
    account = models.ForeignKey(Account, related_name='entries')
    category = models.ForeignKey(Category, related_name='entries')
    type = models.CharField(max_length=2) # 'Dr' or 'Cr'
    amount = models.DecimalField(max_digits=32, decimal_places=2)
    memo = models.CharField(max_length=256, default='', blank=True)

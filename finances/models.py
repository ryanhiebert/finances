from django.db import models

class Journal(models.Model):
    name = models.SlugField(unique=True)

class Category(models.Model):
    class Meta:
        unique_together = (('journal', 'name'),)
    journal = models.ForeignKey(Journal)
    name = models.SlugField()

class Budget(models.Model):
    journal = models.ForeignKey(Journal, related_name='budgets')
    start = models.DateField()
    stop = models.DateField()
    categories = models.ManyToManyField(Category, through='Allotment', related_name='categories')

class Allotment(models.Model):
    class Meta:
        unique_together = (('category', 'budget'),)
    category = models.ForeignKey(Category, related_name='allotments')
    budget = models.ForeignKey(Budget, related_name='allotments')
    amount = models.DecimalField(max_digits=32, decimal_places=2)

class Account(models.Model):
    class Meta:
        unique_together = (('journal', 'name'),)
    journal = models.ForeignKey(Journal, related_name='accounts')
    name = models.SlugField()
    type = models.CharField(max_length=2) # 'Dr' or 'Cr'

class Transaction(models.Model):
    pass

class Entry(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='entries')
    payee = models.CharField(max_length=256, null=True, blank=True)
    account = models.ForeignKey(Account, related_name='entries')
    category = models.ForeignKey(Category, related_name='entries')
    type = models.CharField(max_length=2) # 'Dr' or 'Cr'
    amount = models.DecimalField(max_digits=32, decimal_places=2)

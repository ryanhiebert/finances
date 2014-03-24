from django.contrib import admin
from .models import Journal, Budget, Category, Allotment, Account, Transaction, Entry

class AllotmentInline(admin.TabularInline):
    model = Allotment
    extra = 2

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 2

class JournalAdmin(admin.ModelAdmin):
    pass

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('journal', 'start', 'stop')
    inlines = (AllotmentInline,)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    inlines = (EntryInline,)

admin.site.register(Journal, JournalAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Account, AccountAdmin)

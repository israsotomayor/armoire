from django.contrib import admin

# Register your models here.
from billing.models import ClosingCash, Company, Person, Product, Invoice, Table, Petition, Detail, AccountingEntry, \
    History, Activity, ReceivableAccount, Rol, UserAccount, Fee, Setting

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Table)
admin.site.register(Petition)
admin.site.register(Detail)
admin.site.register(ClosingCash)
admin.site.register(AccountingEntry)
admin.site.register(History)
admin.site.register(Activity)
admin.site.register(ReceivableAccount)
admin.site.register(Rol)
admin.site.register(UserAccount)
admin.site.register(Fee)
admin.site.register(Setting)

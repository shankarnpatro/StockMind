from django.contrib import admin

# Register your models here.
from apps.equity.models import Buy, Sell

admin.site.register(Buy)
admin.site.register(Sell)

from django.contrib import admin

from .models import SalesOrder

@admin.register(SalesOrder)
class OrderAdmin(admin.ModelAdmin):
    pass

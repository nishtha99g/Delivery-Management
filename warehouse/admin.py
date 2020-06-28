from django.contrib import admin
from .models import Warehouse, KeyVal


class KeyValInline(admin.TabularInline):
    model = KeyVal
    raw_id_fields = ['locname']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['location', 'loc_x', 'loc_y', 'zone', 'time_slot']
    # list_filter = ['location']
    inlines = [KeyValInline]

from django.contrib import admin
from menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url')
    list_filter = ('parent',)
    search_fields = ('name', 'url')
    raw_id_fields = ('parent',)

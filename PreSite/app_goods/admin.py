from django.contrib import admin
from app_goods.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'price']

admin.site.register(Item, ItemAdmin)
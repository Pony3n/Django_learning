from django.contrib import admin
from app_media.models import *

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']

admin.site.register(File, FileAdmin)

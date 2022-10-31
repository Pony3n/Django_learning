from django.contrib import admin
from .models import Advertisment
# Register your models here.

@admin.register(Advertisment)
class AdvertismentAdmin(admin.ModelAdmin):
    pass

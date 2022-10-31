from django.contrib import admin
from app_employment.models import *



class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher', 'published_at']

admin.site.register(Vacancy, VacancyAdmin)

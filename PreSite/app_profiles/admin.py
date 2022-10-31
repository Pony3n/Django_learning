from django.contrib import admin
from app_profiles.models import Publisher, Author, Book

class BookInLine(admin.TabularInline):      #Вместо TabularInline(приятнее) -> можно использовать StackedInLine (другой вид\дело вкуса)
    model = Book            #(1)Необходимая команда для появления инициализации объекта

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'country', 'is_active', 'sold_books']
    list_filter = ['id', 'country', 'is_active']
    search_fields = ['country']
    inlines = [BookInLine]          #(1)Добавляет возможность создания нового объекта класса Book в создание Publisher
    fieldsets = (
        ('Локация', {
            'fields': ('city', 'country'),
            'classes': ['collapse']
        }),
        ('Основная информация', {
            'fields': ('name', 'genre', 'sold_books'),
            'classes': ['collapse']
        })
    )

    actions = ['mark_as_active', 'mark_as_not_active']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_not_active(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус "активен"'
    mark_as_not_active.short_description = 'Перевести в статус "не активен"'

class AuthorAdmiin(admin.ModelAdmin):
    list_display = ['name', 'country', 'biography']
    fieldsets = (
        ('Основные сведения', {
            'fields': ('name', 'city', 'country'),
            'description': 'Основные данные автора',      #Описание группы
            'classes': ['collapse']             #show\hide кнопка
        }),
        ('Биографические данные', {
            'fields': ('university', 'birth_date'),
            'description': 'Различные данные из биографии автора',
            'classes': ['collapse']
        }),
        ('Контакты', {
            'fields': ('phone_number', 'personal_page', 'twitter', 'facebook'),
            'description': 'Данные для связи с автором',
            'classes': ['collapse']
        })
    )                                               #Группировка полей по темам (вложенные кортежи)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'publication_date']

    actions = ['mark_as_Draft', 'mark_as_Review', 'mark_as_Published']      #Назначаем кнопки действия(action)

    def mark_as_Draft(self, request, queryset):                 #Прописываем функции, которые выполняют смену статуса
        queryset.update(status='D')

    def mark_as_Review(self, request, queryset):
        queryset.update(status='R')

    def mark_as_Published(self, request, queryset):
        queryset.update(status='P')

    mark_as_Draft.short_description = 'Перевести в статус Черновик'         #Добавляем краткое описание к действию
    mark_as_Review.short_description = 'Перевести в статус Ревью'
    mark_as_Published.short_description = 'Перевести в статус Опубликовано'


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmiin)
admin.site.register(Book, BookAdmin)



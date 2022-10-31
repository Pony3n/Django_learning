from django.db import models

class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    description = models.TextField(default='', verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = "вакансия"
        verbose_name_plural = "вакансии"
        permissions = (                                 #создание отдельного разрешения, как пункта прав в админке пользователя
            ('can_publish', 'Может публиковать'),
        )

    def __str__(self):
        return self.title
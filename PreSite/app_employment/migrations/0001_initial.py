# Generated by Django 4.1.2 on 2022-10-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('publisher', models.CharField(max_length=30, verbose_name='Кто опубликовал')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('published_at', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
                'permissions': (('can_publish', 'Может публиковать'),),
            },
        ),
    ]

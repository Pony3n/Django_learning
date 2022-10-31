# Generated by Django 4.1.2 on 2022-10-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0004_author_birth_date_author_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Ч', 'Черновик'), ('П', 'Правится'), ('О', 'Опубликовано')], default='Ч', max_length=1),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0002_author_rename_country_publisher_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('autrhors', models.ManyToManyField(to='app_profiles.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.publisher')),
            ],
        ),
    ]

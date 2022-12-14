# Generated by Django 4.1.2 on 2022-10-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0005_book_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autrhors',
            new_name='author',
        ),
        migrations.AddField(
            model_name='publisher',
            name='sold_books',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('R', 'Review'), ('P', 'published')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='is_active',
            field=models.BooleanField(verbose_name='статус'),
        ),
    ]

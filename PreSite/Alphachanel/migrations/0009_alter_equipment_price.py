# Generated by Django 4.1.1 on 2022-10-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alphachanel', '0008_alter_advertisment_status_alter_statusadv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.IntegerField(max_length=1000),
        ),
    ]

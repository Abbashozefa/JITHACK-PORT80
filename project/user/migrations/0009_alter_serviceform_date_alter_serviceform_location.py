# Generated by Django 4.1 on 2022-12-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_serviceform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceform',
            name='date',
            field=models.DateField(max_length=200),
        ),
        migrations.AlterField(
            model_name='serviceform',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]

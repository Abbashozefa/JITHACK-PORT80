# Generated by Django 4.1 on 2022-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_serviceform_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceform',
            name='service',
            field=models.CharField(max_length=200),
        ),
    ]

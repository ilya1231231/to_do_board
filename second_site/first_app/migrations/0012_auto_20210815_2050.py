# Generated by Django 3.2.1 on 2021-08-15 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_auto_20210813_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utask',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='utask',
            name='user',
        ),
    ]
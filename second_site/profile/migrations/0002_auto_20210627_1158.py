# Generated by Django 3.2.3 on 2021-06-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]

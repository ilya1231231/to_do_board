# Generated by Django 3.2.1 on 2021-08-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210803_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utask',
            name='task',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='utask',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название'),
        ),
    ]
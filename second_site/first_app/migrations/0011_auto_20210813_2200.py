# Generated by Django 3.2.1 on 2021-08-13 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_auto_20210809_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='utask',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_profile', to='first_app.profile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='utask',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]

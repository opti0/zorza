# Generated by Django 2.0.2 on 2018-03-11 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_times_is_default'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayplan',
            old_name='day',
            new_name='date',
        ),
    ]
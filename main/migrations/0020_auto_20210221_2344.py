# Generated by Django 3.1.5 on 2021-02-21 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_soundtrack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soundtrack',
            old_name='slugTrack',
            new_name='slug',
        ),
    ]

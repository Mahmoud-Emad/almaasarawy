# Generated by Django 3.1.5 on 2021-02-24 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0006_auto_20210224_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soundtrack',
            old_name='slugs',
            new_name='slugTrack',
        ),
    ]

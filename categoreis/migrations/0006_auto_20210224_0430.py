# Generated by Django 3.1.5 on 2021-02-24 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0005_auto_20210224_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soundtrack',
            old_name='slug',
            new_name='slugs',
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-21 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210221_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundtrack',
            name='TrackLink',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
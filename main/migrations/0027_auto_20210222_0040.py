# Generated by Django 3.1.5 on 2021-02-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210222_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundtrack',
            name='TrackLink',
            field=models.CharField(max_length=10000),
        ),
    ]

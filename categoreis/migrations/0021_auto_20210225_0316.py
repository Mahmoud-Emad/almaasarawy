# Generated by Django 3.1.5 on 2021-02-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0020_auto_20210225_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submulticategory',
            name='IsTrack',
        ),
        migrations.AlterField(
            model_name='submulticategory',
            name='TrackLink',
            field=models.CharField(default='', max_length=10000, verbose_name='Track Link'),
            preserve_default=False,
        ),
    ]

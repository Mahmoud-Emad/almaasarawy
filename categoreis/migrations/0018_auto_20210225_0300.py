# Generated by Django 3.1.5 on 2021-02-25 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0017_auto_20210225_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mothercategory',
            name='Chicese_list',
        ),
        migrations.RemoveField(
            model_name='mothercategory',
            name='LinkBook',
        ),
        migrations.RemoveField(
            model_name='mothercategory',
            name='LinkEmbed',
        ),
        migrations.AddField(
            model_name='mothercategory',
            name='BookLink',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Put Link Here'),
        ),
        migrations.AddField(
            model_name='mothercategory',
            name='IsBook',
            field=models.BooleanField(default=False, max_length=255, verbose_name='This is Book Or Page Link?'),
        ),
    ]

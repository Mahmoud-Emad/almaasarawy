# Generated by Django 3.1.5 on 2021-02-25 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0021_auto_20210225_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundtrack',
            name='Chicese_list',
            field=models.CharField(choices=[('Category Page', 'Category Page'), ('Sound Cloud Track', 'Sound Cloud Track'), ('YouTube Video', 'YouTube Video')], default='Category Page', max_length=255, verbose_name='Choice What is it'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='Chicese_list',
            field=models.CharField(choices=[('Category Page', 'Category Page'), ('Sound Cloud Track', 'Sound Cloud Track'), ('YouTube Video', 'YouTube Video')], default='Category Page', max_length=255, verbose_name='Choice What is it'),
        ),
        migrations.AlterField(
            model_name='submulticategory',
            name='Chicese_list',
            field=models.CharField(choices=[('Category Page', 'Category Page'), ('Sound Cloud Track', 'Sound Cloud Track'), ('YouTube Video', 'YouTube Video')], default='Category Page', max_length=255, verbose_name='Choice What is it'),
        ),
    ]

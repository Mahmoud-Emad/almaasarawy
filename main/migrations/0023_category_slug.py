# Generated by Django 3.1.5 on 2021-02-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]

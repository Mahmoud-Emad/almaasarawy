# Generated by Django 3.1.5 on 2021-02-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0009_auto_20210224_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='mothercategory',
            name='LinkIs',
            field=models.CharField(default='', max_length=1055, verbose_name='Put Fall Link if This is #Book, Or This Is YouTube Or Sound Put Link From Src embed'),
            preserve_default=False,
        ),
    ]

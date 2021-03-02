# Generated by Django 3.1.6 on 2021-02-20 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210221_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorybooks',
            name='Book_link',
            field=models.CharField(default='', max_length=50, verbose_name='Book Link (Please Put Fall Download Path)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorybooks',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Book name'),
        ),
    ]

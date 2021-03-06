# Generated by Django 3.1.5 on 2021-02-24 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoreis', '0007_auto_20210224_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundtrack',
            name='TitleEnglish',
            field=models.CharField(default='', max_length=255, verbose_name='English Category Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soundtrack',
            name='Title',
            field=models.CharField(max_length=255, verbose_name='Category Title'),
        ),
        migrations.AlterField(
            model_name='soundtrack',
            name='TrackLink',
            field=models.CharField(max_length=10000, verbose_name='Track Link'),
        ),
        migrations.AlterField(
            model_name='soundtrack',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Tracks', to='categoreis.submulticategory'),
            preserve_default=False,
        ),
    ]

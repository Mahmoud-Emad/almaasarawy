# Generated by Django 3.1.5 on 2021-02-21 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210221_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('slugTrack', models.SlugField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tracks', to='main.category')),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackYouTube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Track name')),
                ('Slug', models.SlugField(blank=True, null=True, verbose_name='let this feild empty')),
                ('Track', models.CharField(max_length=50, verbose_name='Track link')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SYoutube', to='main.subcategory')),
            ],
        ),
    ]

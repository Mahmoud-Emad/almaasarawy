# Generated by Django 3.1.6 on 2021-02-20 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210221_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryYoutube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.categoryyoutube')),
            ],
        ),
    ]
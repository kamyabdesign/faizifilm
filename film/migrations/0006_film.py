# Generated by Django 3.1.7 on 2021-04-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_video_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('link', models.URLField(blank=True)),
                ('pic', models.ImageField(upload_to='video_pic')),
            ],
        ),
    ]

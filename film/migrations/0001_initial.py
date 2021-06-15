# Generated by Django 3.1.7 on 2021-04-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hestory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('yeras', models.IntegerField(blank=True)),
                ('picture', models.ImageField(upload_to='hestory')),
                ('work_title', models.CharField(max_length=150)),
                ('work_detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='main')),
                ('tiwitter', models.URLField(blank=True, max_length=150)),
                ('facebook', models.URLField(blank=True, max_length=150)),
                ('youtube', models.URLField(blank=True, max_length=150)),
                ('instagram', models.URLField(blank=True, max_length=150)),
                ('telegram', models.URLField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=250)),
                ('team_pic', models.ImageField(upload_to='team_pic')),
                ('tiwitter', models.URLField(blank=True, max_length=150)),
                ('facebook', models.URLField(blank=True, max_length=150)),
                ('instagram', models.URLField(blank=True, max_length=150)),
                ('telegram', models.URLField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Trust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('image_1', models.ImageField(upload_to='trust')),
                ('image_2', models.ImageField(upload_to='trust')),
                ('image_3', models.ImageField(upload_to='trust')),
                ('image_4', models.ImageField(upload_to='trust')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]

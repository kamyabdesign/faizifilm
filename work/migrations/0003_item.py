# Generated by Django 3.1.7 on 2021-04-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20210420_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to='logo')),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
                ('telegram', models.URLField()),
                ('instagram', models.URLField()),
                ('social_img1', models.ImageField(upload_to='social')),
                ('social_img2', models.ImageField(upload_to='social')),
                ('social_img3', models.ImageField(upload_to='social')),
                ('social_img4', models.ImageField(upload_to='social')),
                ('social_img5', models.ImageField(upload_to='social')),
                ('social_img6', models.ImageField(upload_to='social')),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ImageField(default='default/avatar.jpg', upload_to='comments', verbose_name='تصویر'),
        ),
    ]

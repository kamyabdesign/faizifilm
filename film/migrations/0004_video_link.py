# Generated by Django 3.1.7 on 2021-04-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20210426_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
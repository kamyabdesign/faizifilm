# Generated by Django 3.1.7 on 2021-04-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_main_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='hestory',
            name='data_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

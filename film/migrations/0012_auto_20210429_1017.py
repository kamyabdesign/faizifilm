# Generated by Django 3.1.7 on 2021-04-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0011_auto_20210429_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hestory',
            name='data_date',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

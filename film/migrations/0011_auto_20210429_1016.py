# Generated by Django 3.1.7 on 2021-04-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_auto_20210429_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hestory',
            name='yeras',
            field=models.IntegerField(blank=True),
        ),
    ]

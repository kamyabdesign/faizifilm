# Generated by Django 3.1.7 on 2021-05-29 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alls_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alls',
            name='dates',
        ),
    ]

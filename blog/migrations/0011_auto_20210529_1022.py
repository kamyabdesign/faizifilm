# Generated by Django 3.1.7 on 2021-05-29 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210526_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alls',
            old_name='time',
            new_name='dates',
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_all'),
        ('work', '0004_work_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.ManyToManyField(related_name='work', to='blog.Category'),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-30 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0002_auto_20180130_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
        migrations.RemoveField(
            model_name='ranking',
            name='author',
        ),
    ]

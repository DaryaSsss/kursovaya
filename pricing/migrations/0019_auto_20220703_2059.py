# Generated by Django 3.2 on 2022-07-03 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0018_auto_20220703_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalplacebooking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='placebooking',
            name='date',
        ),
    ]

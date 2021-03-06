# Generated by Django 4.0.2 on 2022-03-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_rename_places_workplace_alter_workplace_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('desc', models.CharField(max_length=250, verbose_name='Desc')),
                ('free', models.BooleanField(verbose_name='Free')),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
        ),
    ]

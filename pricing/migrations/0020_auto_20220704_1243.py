# Generated by Django 3.2 on 2022-07-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0019_auto_20220703_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalplacebooking',
            name='_in',
            field=models.CharField(default='01/01/2022', help_text='When the booking ends.', max_length=50, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='historicalplacebooking',
            name='out',
            field=models.CharField(default='01/01/2022', help_text='When the booking starts.', max_length=50, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='placebooking',
            name='_in',
            field=models.CharField(default='01/01/2022', help_text='When the booking ends.', max_length=50, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='placebooking',
            name='out',
            field=models.CharField(default='01/01/2022', help_text='When the booking starts.', max_length=50, verbose_name='Start'),
        ),
    ]
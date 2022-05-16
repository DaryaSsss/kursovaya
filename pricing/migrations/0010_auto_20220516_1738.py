# Generated by Django 3.0 on 2022-05-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0009_historicalworkplacebooking_historicalworkplace_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmeetingrooms',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalmeetingroomsbooking',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalofficebooking',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicaloffices',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalworkplace',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalworkplacebooking',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='meetingrooms',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='meetingroomsbooking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='officebooking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='offices',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='workplacebooking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

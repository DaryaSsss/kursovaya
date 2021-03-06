# Generated by Django 4.0.2 on 2022-03-15 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0004_meetingrooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkplaceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.CharField(max_length=50, verbose_name='People name')),
                ('date', models.DurationField()),
                ('paid', models.BooleanField(verbose_name='Paid')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.workplace')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.CharField(max_length=50, verbose_name='People name')),
                ('date', models.DurationField()),
                ('paid', models.BooleanField(verbose_name='Paid')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.offices')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoomsBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.CharField(max_length=50, verbose_name='People name')),
                ('date', models.DurationField()),
                ('paid', models.BooleanField(verbose_name='Paid')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.meetingrooms')),
            ],
        ),
    ]

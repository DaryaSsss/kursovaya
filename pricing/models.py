from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User


class Workplace(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Workplace'
        verbose_name_plural = 'Workplaces'

    def __str__(self):
        return self.name


class Offices(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'

    def __str__(self):
        return self.name

class MeetingRooms(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'MeetingRoom'
        verbose_name_plural = 'MeetingRooms'

    def __str__(self):
        return self.name

class WorkplaceBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254, default=' ')
    place = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.BooleanField('Paid')
    history = HistoricalRecords()

    def get_absolute_url(self):
        return f'/pricing/bookworkplace/{self.id}'

    def __str__(self):
        return self.place.name

class OfficeBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Offices, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254)
    date = models.DateField()
    paid = models.BooleanField('Paid')
    history = HistoricalRecords()

    def get_absolute_url(self):
        return f'/pricing/bookoffice/{self.id}'

    def __str__(self):
        return self.place.name

class MeetingRoomsBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(MeetingRooms, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254, default='')
    date = models.DateField()
    paid = models.BooleanField('Paid')
    history = HistoricalRecords()

    def get_absolute_url(self):
        return f'/pricing/bookmeetingroom/{self.id}'

    def __str__(self):
        return self.place.name

class Places(models.Model):
    PLACES_TYPES = (
        ('W', 'Workplace'),
        ('O', 'Office'),
        ('MR', 'Meeting Room')
    )
    name = models.CharField('Name', max_length=50)
    place_type = models.CharField(max_length=2, choices=PLACES_TYPES)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.name

class PlaceBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254, default='')
    date = models.DateField()
    paid = models.BooleanField('Paid')
    history = HistoricalRecords()

    def get_absolute_url(self):
        return f'/pricing/bookplace/{self.id}'

    def __str__(self):
        return self.place.name
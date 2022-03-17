from django.db import models

class Workplace(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')

    class Meta:
        verbose_name = 'Workplace'
        verbose_name_plural = 'Workplaces'

    def __str__(self):
        return self.name


class Offices(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'

    def __str__(self):
        return self.name

class MeetingRooms(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Desc', max_length=250)
    free = models.BooleanField('Free')

    class Meta:
        verbose_name = 'MeetingRoom'
        verbose_name_plural = 'MeetingRooms'

    def __str__(self):
        return self.name

class WorkplaceBooking(models.Model):
    people = models.CharField('People name', max_length=50)
    email = models.EmailField('Email', max_length=254, default=' ')
    place = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.BooleanField('Paid')

    def get_absolute_url(self):
        return f'/pricing/bookworkplace/{self.id}'

    def __str__(self):
        return self.people

class OfficeBooking(models.Model):
    people = models.CharField('People name', max_length=50)
    place = models.ForeignKey(Offices, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254)
    date = models.DateField()
    paid = models.BooleanField('Paid')

    def get_absolute_url(self):
        return f'/pricing/bookoffice/{self.id}'

    def __str__(self):
        return self.people

class MeetingRoomsBooking(models.Model):
    people = models.CharField('People name', max_length=50)
    place = models.ForeignKey(MeetingRooms, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254, default='')
    date = models.DateField()
    paid = models.BooleanField('Paid')

    def get_absolute_url(self):
        return f'/pricing/bookmeetingroom/{self.id}'

    def __str__(self):
        return self.people


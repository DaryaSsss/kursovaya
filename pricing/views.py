from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Workplace, Offices, MeetingRooms
from .forms import WorkplaceForm, OfficeForm, MeetingRoomForm

def pricing_home(request):
    return render(request, 'pricing/pricing_home.html')


def workplaces(request):
    workplaces = Workplace.objects.all().filter(free='True')
    return render(request, 'pricing/workplaces.html', {'workplaces': workplaces})

def offices(request):
    offices = Offices.objects.all().filter(free='True')
    return render(request, 'pricing/offices.html', {'offices': offices})

def meetingrooms(request):
    meetingrooms = MeetingRooms.objects.all().filter(free='True')
    return render(request, 'pricing/meetingrooms.html', {'meetingrooms': meetingrooms})



def bookworkplace(request, pk):
    workplace = Workplace.objects.all().get(id=pk)
    error = ''

    if request.method == 'POST':
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.paid = True
            workplace.free = False
            workplace.save()
            instance.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = WorkplaceForm()

    data = {
        'form': form,
        'error': error,
        'workplace': workplace.name,
    }

    return render(request, 'pricing/bookworkplace.html', data)

def bookoffice(request, pk):
    office = Offices.objects.all().get(id=pk)
    error = ''
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.paid = True
            office.free = False
            office.save()
            instance.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = OfficeForm()

    data = {
        'form': form,
        'error': error,
        'office': office.name
    }
    return render(request, 'pricing/bookoffice.html', data)

def bookmeetingroom(request, pk):
    meetingroom = MeetingRooms.objects.all().get(id=pk)
    error = ''
    if request.method == 'POST':
        form = MeetingRoomForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.paid = True
            meetingroom.free = False
            meetingroom.save()
            instance.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = MeetingRoomForm()

    data = {
        'form': form,
        'error': error,
        'meetingroom': meetingroom
    }
    return render(request, 'pricing/bookmeetingroom.html', data)
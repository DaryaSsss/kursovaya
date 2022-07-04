from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Workplace, Offices, MeetingRooms, Places
from .forms import WorkplaceForm, OfficeForm, MeetingRoomForm, PlaceForm
from django.core.paginator import Paginator



def pricing_home(request):
    return render(request, 'pricing/pricing_home.html')


def workplaces(request):
    workplaces = Workplace.objects.all().filter(free='True')
    paginator = Paginator(workplaces, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pricing/workplaces.html', {'workplaces': workplaces, 'page_obj': page_obj},)

def offices(request):
    offices = Offices.objects.all().filter(free='True')
    return render(request, 'pricing/offices.html', {'offices': offices})

def meetingrooms(request):
    meetingrooms = MeetingRooms.objects.all().filter(free='True')
    return render(request, 'pricing/meetingrooms.html', {'meetingrooms': meetingrooms})



def bookworkplace(request, pk):
    current_user = request.user
    workplace = Workplace.objects.all().get(id=pk)
    error = ''

    if request.method == 'POST':
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.user_id = current_user.id
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
    current_user = request.user
    office = Offices.objects.all().get(id=pk)
    error = ''
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.user_id = current_user.id
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
    current_user = request.user
    meetingroom = MeetingRooms.objects.all().get(id=pk)
    error = ''
    if request.method == 'POST':
        form = MeetingRoomForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.user_id = current_user.id
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

def bookplace(request, pk):
    current_user = request.user
    place = Places.objects.all().get(id=pk)
    error = ''
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place_id = pk
            instance.user_id = current_user.id
            instance.paid = True
            place.free = False
            place.save()
            instance.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = PlaceFrom()

    data = {
        'form': form,
        'error': error,
        'place': place
    }
    return render(request, 'pricing/bookplace.html', data)
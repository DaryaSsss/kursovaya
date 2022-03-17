from .models import WorkplaceBooking, OfficeBooking, MeetingRoomsBooking
from django.forms import ModelForm, TextInput, DateInput, Textarea, EmailInput

class WorkplaceForm(ModelForm):
    class Meta:
        model = WorkplaceBooking
        fields = ['people', 'date', 'email']
        widgets = {
            "people": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            "email": EmailInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Booking time',
            })
        }
class OfficeForm(ModelForm):
    class Meta:
        model = OfficeBooking
        fields = ['people', 'date', 'email']
        widgets ={
            "people": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Booking time',
            })
        }
class MeetingRoomForm(ModelForm):
    class Meta:
        model = MeetingRoomsBooking
        fields = ['people', 'date', 'email']
        widgets ={
            "people": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Booking time',
            })
        }
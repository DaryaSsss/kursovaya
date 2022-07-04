from django.urls import path
from . import views

urlpatterns = [
    path('', views.pricing_home, name='pricing_home'),
    path('workplaces', views.workplaces, name='workplaces'),
    path('offices', views.offices, name='offices'),
    path('meetingrooms', views.meetingrooms, name='meetingrooms'),
    path('bookworkplace/<int:pk>', views.bookworkplace, name='bookworkplace'),
    path('bookplace/<int:pk>', views.bookplace, name='bookworkplace'),
    path('bookoffice/<int:pk>', views.bookoffice, name='bookoffice'),
    path('bookmeetingroom/<int:pk>', views.bookmeetingroom, name='bookmeetingroom'),
]

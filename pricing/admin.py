from django.contrib import admin
from .models import Workplace
from .models import Offices
from .models import MeetingRooms
from .models import WorkplaceBooking
from .models import OfficeBooking
from .models import MeetingRoomsBooking

admin.site.register(Workplace)
admin.site.register(Offices)
admin.site.register(MeetingRooms)
admin.site.register(WorkplaceBooking)
admin.site.register(OfficeBooking)
admin.site.register(MeetingRoomsBooking)
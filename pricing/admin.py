from django.contrib import admin
from .models import Workplace
from .models import Offices
from .models import MeetingRooms
from .models import WorkplaceBooking
from .models import OfficeBooking
from .models import MeetingRoomsBooking
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ExportActionMixin

class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('place', 'email', 'paid', 'date')

class HistoryExportAdmin(SimpleHistoryAdmin, BookAdmin):
    pass


admin.site.register(Workplace, SimpleHistoryAdmin)
admin.site.register(Offices, SimpleHistoryAdmin)
admin.site.register(MeetingRooms, SimpleHistoryAdmin)
admin.site.register(WorkplaceBooking, HistoryExportAdmin)
admin.site.register(OfficeBooking, HistoryExportAdmin)
admin.site.register(MeetingRoomsBooking, HistoryExportAdmin)
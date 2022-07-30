from atexit import register
from pydoc import Doc
from django.contrib import admin
from .models import Departments
from .models import Doctors, Booking, Contact, About

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'patient_phone', 'patient_email', 'doc_name', 'booking_date', 'booked_on')
admin.site.register(Booking, BookingAdmin)

admin.site.register(Contact)
admin.site.register(About)
from django.contrib import admin
from scheduler.models import Module, Booking, Slot, Shift, Schedule, Student

# Register your models here.
admin.site.register(Module)
admin.site.register(Booking)
admin.site.register(Slot)
admin.site.register(Student)
admin.site.register(Shift)
admin.site.register(Schedule)

from rest_framework import serializers
from scheduler.models import Module, Booking, Slot, Student, Schedule

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["code", "moduleID", "name"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["lecturer", "lab", "module"]

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ["id", "booking", "day", "shift", "unavailable", "blocking_modules"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["student_number", "first_name", "last_name", "role", "modules", "shifts"]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
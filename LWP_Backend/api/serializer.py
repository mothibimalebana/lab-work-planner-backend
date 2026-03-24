from rest_framework import serializers
from scheduler.models import Module, Booking, Slot, Student, Schedule

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["code", "moduleID", "name"]
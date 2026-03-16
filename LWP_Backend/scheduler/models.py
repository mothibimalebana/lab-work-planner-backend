from django.db import models

# Create your models here.
class Module(models.Model):
    code = models.CharField(unique=True)
    moduleID = models.IntegerField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.code

class Booking(models.Model):
    lecturer = models.CharField(max_length=255)
    lab = models.IntegerField()
    module = models.OneToOneField(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.module

class Slot(models.Model):
    slotID = models.IntegerField(primary_key=True, unique=True, editable=False)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    unavailable = models.BooleanField
    def __str__(self):
        return self.slotID

class Role(models.TextChoices):
    SUPERVISOR = "Supervisor"
    ASSISTANT = "Assistant"

class Students(models.Model):
    student_number = models.IntegerField(primary_key=True, editable=False ,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(choices=Role.choices, default=Role.ASSISTANT)
    modules = models.ManyToManyField(Module)
    shifts = models.ManyToManyField(Slot)
    def __str__(self):
        return self.student_number
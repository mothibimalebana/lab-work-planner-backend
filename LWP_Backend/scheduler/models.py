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
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    day = models.IntegerField()
    shift = models.IntegerField()
    unavailable = models.BooleanField
    class Meta:
        unique_together = ['day', 'shift']
        ordering = ['day', 'shift']

    def __str__(self):
        return f"day ${self.day}, shift ${self.shift}"

Lab_Role = [
    ('A', 'Lab Assistant'),
    ('S', 'Lab Supervisor')
]

class Students(models.Model):
    student_number = models.IntegerField(primary_key=True, editable=False ,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=Lab_Role, default=1)
    modules = models.ManyToManyField(Module)
    shifts = models.ManyToManyField(Slot)
    def __str__(self):
        return f"{self.student_number}"

class Schedule(models.Model):
    name = models.CharField(max_length=255)
    matrix = models.JSONField(default=list)

    def __str__(self):
        return self.name        
        



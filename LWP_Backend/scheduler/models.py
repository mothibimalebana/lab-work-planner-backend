from django.db import models

# Create your models here.
class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=8, unique=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.code

class Booking(models.Model):
    lecturer = models.CharField(max_length=255, null=True, blank=True)
    lab = models.IntegerField()
    module = models.OneToOneField(Module, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.module} in lab: {self.lab}"

class Slot(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    booking = models.OneToOneField(Booking,  null=True, blank=True, on_delete=models.SET_NULL)
    day = models.IntegerField()
    shift = models.IntegerField()
    unavailable = models.BooleanField(default=False)
    blocking_modules= models.ManyToManyField(Module)
    class Meta:
        unique_together = ['day', 'shift']
        ordering = ['day', 'shift']

    def __str__(self):
        return f"day {self.day}, shift {self.shift}"

Lab_Role = [
    ('A', 'Lab Assistant'),
    ('S', 'Lab Supervisor')
]

class Student(models.Model):
    student_number = models.IntegerField(primary_key=True, editable=False ,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=Lab_Role, default='A')
    modules = models.ManyToManyField(Module)
    shifts = models.ManyToManyField(Slot)
    def __str__(self):
        return f"{self.student_number}"

class Shift(models.Model):
    shift_id = models.IntegerField(unique=True, primary_key=True)
    supervisor = models.ForeignKey(Student,on_delete=models.SET_NULL, related_name='shift_supervisor', null=True, blank=True)
    assistants = models.ManyToManyField(Student, related_name='shift_assistant')

    def __str__(self):
        return f"slot: {self.shift_id}, supervisor: {self.supervisor}, assistants: {self.assistants}"

class Schedule(models.Model):
    name = models.CharField(max_length=255)
    matrix = models.JSONField(default=list)

    def __str__(self):
        return self.name

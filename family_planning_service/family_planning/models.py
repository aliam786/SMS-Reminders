from django.db import models
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
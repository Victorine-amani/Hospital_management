from django.db import models
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.

class MedicalRecord(models.Model):
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date=models.DateField()
    particulars=models.TextField()
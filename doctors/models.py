from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50 )
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=50)
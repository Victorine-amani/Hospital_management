from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50 )
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=100)

# Create your models here.


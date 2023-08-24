from django import forms
from.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['first_name', 'last_name', 'email', 'phone_number','address','speciality']
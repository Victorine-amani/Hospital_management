from django.shortcuts import render
from django.shortcuts import render, redirect
from.models import Patient
from.forms import PatientForm
from django.contrib.auth.decorators import login_required
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.


def home(request):
    return render(request,'home.html')


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patients:patients')
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})

def patients(request):
    patient=Patient.objects.all()
    return render(request, 'patients.html',{'patient':patient})
    

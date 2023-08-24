from django.shortcuts import render, redirect
from.models import Doctor
from.forms import DoctorForm
from django.http import HttpResponse
from django import forms
# Create your views here.

def home(request):
    return render(request,'home.html')

def doctors(request):
    doctor=Doctor.objects.all()
    return render(request, 'doctors.html',{'doctor':doctor})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctors')
        else:
             print(form.errors)
    else:
            form = DoctorForm()
    return render(request, 'create_doctor.html',{'form':form})



from django.shortcuts import render, redirect
from.models import MedicalRecord
from.forms import MedicalRecordForm

# Create your views here.


def home(request):
    return render(request,'home.html')

def medical_records(request):
    medical_record=MedicalRecord.objects.all()
    return render(request, 'medical_records.html',{'medical_record':medical_record})


def create_record(request):
    if request.method == 'POST':
       form = MedicalRecordForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('records:records')
    else:
          form = MedicalRecordForm()
    return render(request, 'create_record.html',{'form':form})

from django.shortcuts import render, redirect
from.models import Visit
from.forms import VisitForm

# Create your views here.


def home(request):
    return render(request,'home.html')

def create_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visits:visits')
    else:
            form = VisitForm()
    return render(request, 'create_visit.html',{'form':form})



def visits(request):
    visit=Visit.objects.all()
    return render(request, 'visits.html',{'visit':visit})
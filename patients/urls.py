from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 


app_name="patients"
urlpatterns = [
    path('', views.home, name='home'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('patients/', views.patients, name='patients')
    ]
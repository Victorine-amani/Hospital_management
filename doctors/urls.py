from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 
 
app_name="doctors"
urlpatterns = [
    path('', views.home, name='home'),
    path('create_doctor/', views.create_doctor, name='create_doctor'),
    path('doctors/', views.doctors, name='doctors')
    
 ]
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 


app_name="records"
urlpatterns = [
    path('', views.home, name='home'),
    path('create_record/', views.create_record, name='create_record'),
    path('records/', views.medical_records, name='records')
    ]
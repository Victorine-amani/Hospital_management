from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views 


app_name="visits"
urlpatterns = [
    path('', views.home, name='home'),
    path('create_visit', views.create_visit, name='create_visit'),
    path('visits/', views.visits, name='visits')
    ]
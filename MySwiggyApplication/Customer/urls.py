from django.contrib import admin
from django.urls import path,include
from Customer import views

urlpatterns = [

    path('',views.offermenu,name='offermenu'),
    ]
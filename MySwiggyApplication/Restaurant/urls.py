from django.contrib import admin
from django.urls import path

from Restaurant import views

urlpatterns = [

    path('',views.showMain,name="restro"),
    path('register/',views.registerPage,name="register"),
    path('save_res/',views.save_res,name="save_res"),

]
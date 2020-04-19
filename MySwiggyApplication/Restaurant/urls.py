from django.contrib import admin
from django.urls import path

from Restaurant import views

urlpatterns = [

    path('',views.showMain,name="restro"),
    path('register/',views.registerPage,name="register"),
    path('save_res/',views.save_res,name="save_res"),
    path('restro_login/', views.restro_login, name="restro_login"),
    path('restro_login_check/', views.restro_login_check, name="restro_login_check"),
    path('restro_home/', views.restro_home, name="restro_home"),
]
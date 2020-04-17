from django.contrib import admin
from django.urls import path

from adminpage import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('open_state/',views.open_state,name="open_state"),
    path('save_state/', views.save_state, name="save_state"),
    path('update_state/', views.update_state, name="update_state"),
    path('update_state_data/', views.update_state_data, name="update_state_data"),
    path('delete_state/', views.delete_state, name='delete_state'),
    path('open_city/', views.open_city, name="open_city"),
    path('save_city/', views.save_city, name="save_city"),
    path('update_city/', views.update_city, name="update_city"),
    path('update_city_data/', views.update_city_data, name="update_city_data"),
    path('delete_city/', views.delete_city, name='delete_city'),
    path('open_area/', views.open_area, name="open_area"),
    path('save_area/', views.save_area, name="save_area"),
    path('update_area/', views.update_area, name="update_area"),
    path('update_area_data/', views.update_area_data, name="update_area_data"),
    path('delete_area/', views.delete_area, name='delete_area'),
    path('open_type/', views.open_type, name="open_type"),
    path('save_type/', views.save_type, name="save_type"),
    path('update_type/', views.update_type, name="update_type"),
    path('update_type_data/', views.update_type_data, name="update_type_data"),
    path('delete_type/', views.delete_type, name='delete_type'),
    path('show_pending_res/', views.pending_res, name="show_pending_res"),
    path('show_approved_res/', views.show_approved_res, name="show_approved_res"),
    path('show_cancel_res/', views.show_cancel_res, name="show_cancel_res"),
    path('approve_res/', views.approve_res, name="approve_res"),
    path('cancel_res/', views.cancel_res, name="cancel_res"),
    ]
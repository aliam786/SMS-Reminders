# send_sms/models.py
from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
]
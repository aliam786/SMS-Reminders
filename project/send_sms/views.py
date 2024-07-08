from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(appointment_date__gte=timezone.now())
    return render(request, 'send_sms/appointment_list.html', {'appointments': appointments})

@login_required
def add_appointment(request):
    if request.method == "POST":
        patient_fname = request.POST.get('patient_fname')
        patient_lname = request.POST.get('patient_lname')
        phone_number = request.POST.get('phone_number')
        appointment_date = request.POST.get('appointment_date')
        notes = request.POST.get('notes')
        Appointment.objects.create(
            patient_fname=patient_fname,
            patient_lname=patient_lname,
            phone_number=phone_number,
            appointment_date=appointment_date,
            notes=notes
        )
        return redirect('appointment_list')
    return render(request, 'send_sms/add_appointment.html')


def home(request):
    return redirect('login')
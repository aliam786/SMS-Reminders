# family_planning/tasks.py
from celery import shared_task
from twilio.rest import Client
from django.utils import timezone
from .models import Appointment
from datetime import datetime, timedelta
import os


@shared_task
def check_and_send_sms():
    now = datetime.now()
    # Logic to fetch appointments: Get all appointments that are scheduled for tomorrow
    appointments = Appointment.objects.filter(appointment_date__lte=timezone.now() + timedelta(days=1))
    for appointment in appointments:
        send_sms(appointment)

def send_sms(appointment):
    """
    Sends an SMS reminder for the given appointment using Twilio.

    Args:
        appointment (Appointment): The appointment object containing the details of the appointment.

    Returns:
        None
    """
    # Twilio setup
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = f"Mpore Clinic: Hello {appointment.patient_name}, this is a reminder for your appointment on {appointment.appointment_date}" + (appointment.notes if appointment.notes else "."),
        from_='+12568576097',  # Your Twilio number
        to="+"+appointment.phone_number  # Appointment model has a field for phone number
    )
    print(f"Message sent: {message.sid}")
    appointment.delete()
    print('Appointment deleted')


#imports
from twilio.rest import Client
from django.utils import timezone
from family_planning.models import Appointment
from datetime import datetime, timedelta
import os
from twilio.http.http_client import TwilioHttpClient
from family_planning.models import Appointment
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Check for relevant SMS, Send them, and then delete the DB entry"

    def handle(self, *args, **options):
        proxy_client = TwilioHttpClient(proxy={'http': os.environ.get('http_proxy'), 'https': os.environ.get('https_proxy')})

        def check_and_send_sms():
            # Logic to fetch appointments: Get all appointments that are scheduled for tomorrow
            appointments = Appointment.objects.filter(appointment_date__lte=timezone.now() + timedelta(days=1))
            for appointment in appointments:
                send_sms(appointment)
            else:
                print("no appts")

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
            client = Client(account_sid, auth_token, http_client=proxy_client)

            message = client.messages.create(
                body=f"Mpore Clinic: Hello {appointment.patient_name}, this is a reminder for your appointment on {appointment.appointment_date}" + (". " + appointment.notes if appointment.notes else "."),
                from_='+12568576097',  # Your Twilio number
                to="+" + appointment.phone_number  # Appointment model has a field for phone number
            )
            print(f"Message sent: {message.sid}")
            appointment.delete()
            print('Appointment deleted')

        check_and_send_sms()
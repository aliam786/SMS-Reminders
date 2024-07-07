from django.test import TestCase
from django.utils import timezone
from datetime import datetime, timedelta
from unittest.mock import patch
from .models import Appointment
from .tasks import check_and_send_sms

class CheckAndSendSMSTestCase(TestCase):
    def setUp(self):
        # Create a test appointment for tomorrow
        tomorrow = timezone.now() + timedelta(minutes=1)
        self.appointment = Appointment.objects.create(
            appointment_date=tomorrow,
            patient_name="John Doe",
            phone_number="+1234567890"
        )

    @patch('family_planning.tasks.send_sms')
    def test_check_and_send_sms(self, mock_send_sms):
        # Call the task
        check_and_send_sms()

        # Assert that send_sms was called with the appointment
        mock_send_sms.assert_called_once_with(self.appointment)
        print(f"Message sent")
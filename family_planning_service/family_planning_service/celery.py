# family_planning_service/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'family_planning_service.settings')

app = Celery('family_planning_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule = {
    'check-and-send-sms-every-hr': {
        'task': 'family_planning.tasks.check_and_send_sms',
        'schedule': crontab(hour = '*'),  # 
    },
}

#relevant celery commands
#celery -A family_planning_service beat --loglevel=info
#celery -A family_planning_service worker --loglevel=info
#celery -A family_planning_service flower | http://localhost:5555
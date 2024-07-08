from django.contrib import admin

# Register your models here.

# Import your models here
from .models import Appointment
# Register your models with the admin site

admin.site.register(Appointment)

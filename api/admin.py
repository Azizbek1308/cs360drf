from django.contrib import admin
from .models import Location, WeatherReading
# Register your models here.
admin.site.register(Location)
admin.site.register(WeatherReading)
from django.db import models

class Location(models.Model):
    city_name = models.CharField(max_length=100, unique=True) # e.g., "Tashkent"

    def __str__(self):
        return self.city_name

class WeatherReading(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='readings')
    temperature = models.IntegerField() # You just type "38"
    condition = models.CharField(max_length=50) # You just type "Sunny" or "Hot"
    updated_at = models.DateTimeField(auto_now=True) # Django handles the clock automatically

    class Meta:
        ordering = ['-updated_at'] # Keeps the newest update at the top

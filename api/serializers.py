from rest_framework import serializers
from .models import Location, WeatherReading

class WeatherReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReading
        fields = ['temperature', 'condition', 'updated_at']

class LocationSerializer(serializers.ModelSerializer):
    current_weather = serializers.SerializerMethodField()
    # This automatically serializes all historical entries linked to this city
    historical_logs = WeatherReadingSerializer(source='readings', many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'city_name', 'current_weather', 'historical_logs']

    def get_current_weather(self, obj):
        last_reading = obj.readings.first()
        if last_reading:
            return WeatherReadingSerializer(last_reading).data
        return {"message": "No weather data added yet"}

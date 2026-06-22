from django.http import JsonResponse
from .models import Location
from .serializers import LocationSerializer

def weather_view(request):
    city_name = request.GET.get('city_name')
    unit = request.GET.get('unit', 'C')

    if city_name:
        try:
            location = Location.objects.get(city_name=city_name)
            last_reading = location.readings.first()

            if not last_reading:
                return JsonResponse(
                    {'message': 'No weather data added yet'},
                    status=404
                )

            temperature = last_reading.temperature

            if unit.lower() == 'fahrenheit':
                temperature = (temperature * 9 / 5) + 32
                temperature = f"{temperature:.2f} °F"
            else:
                temperature = f"{temperature:.2f} °C"

            data = {
                "city_name": location.city_name,
                "temperature": temperature,
                "condition": last_reading.condition
            }

            return JsonResponse(data)

        except Location.DoesNotExist:
            return JsonResponse(
                {'message': 'City not found'},
                status=404
            )

    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return JsonResponse(serializer.data, safe=False)
# views.py
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # 1. Start with all locations
        queryset = Location.objects.all()  # This is the base queryset for all locations
        
        # 2. Look for '?city_name=' inside the URL
        city_param = self.request.query_params.get('city_name', None)
        
        if city_param is not None:
            # 3. Filter the database cleanly (case-insensitive)
            queryset = queryset.filter(city_name__iexact=city_param.strip())
            
        return queryset

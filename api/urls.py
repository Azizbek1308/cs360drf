# urls.py
from django.urls import path
from .views import WeatherViewSet  

urlpatterns = [
    path('weather/', WeatherViewSet.as_view({'get': 'list'}), name='weather-list'),
    path('weather/<str:city_name>/', WeatherViewSet.as_view({'get': 'retrieve'}), name='weather-detail'),
]

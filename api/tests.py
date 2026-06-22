#testing API which is created in models.py, serializers.py, views.py and urls.py
from urllib import response

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Location, WeatherReading
class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(city_name="Tashkent")
        WeatherReading.objects.create(location=self.location, temperature=38, condition="Sunny")

    # def test_get_all_city_weather(self):
    #     response = self.client.get('/api/weather/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['city_name'], "Tashkent")
    #     self.assertEqual(response.data[0]['current_weather']['temperature'], 38)
    #     self.assertEqual(response.data[0]['current_weather']['condition'], "Sunny")


    # def test_get_weather_by_city_name(self):
    #     response = self.client.get('/api/weather/', {'city_name': 'Tashkent'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['city_name'], "Tashkent")
    #     self.assertEqual(response.data[0]['current_weather']['temperature'], 38)
    #     self.assertEqual(response.data[0]['current_weather']['condition'], "Sunny")
    
    # def test_get_weather_by_city_name_not_found(self):
    #     response = self.client.get('/api/weather/', {'city_name': 'NonExistentCity'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 0)
    
    # def test_celsius_to_fahrenheit_endpoint_not_found(self):
    #     response = self.client.get('/api/celsius-to-fahrenheit/25/')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.content.decode(), 'Celsius to Fahrenheit conversion is not implemented yet.')
    
    # def test_celsius_to_fahrenheit_endpoint(self):
    #     response = self.client.get('/api/celsius-to-fahrenheit/25/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.content.decode(), '77.00 °F')

    def test_get_weather_in_fahrenheit(self):
        response = self.client.get(
        '/api/weather/',
        {'city_name': 'Tashkent', 'unit': 'fahrenheit'}
        )

        self.assertEqual(  response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['city_name'], "Tashkent")
        self.assertEqual(response.json()['temperature'], "100.40 °F")
        self.assertEqual(response.json()['condition'], "Sunny")



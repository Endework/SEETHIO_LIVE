from django.test import TestCase

# Create your tests here.
# flight_search/tests.py
from django.test import TestCase
from django.urls import reverse

class FlightSearchTests(TestCase):
    def test_search_flights_view(self):
        response = self.client.get(reverse('search_flights'))
        self.assertEqual(response.status_code, 200)
        # Add more tests based on your application's behavior

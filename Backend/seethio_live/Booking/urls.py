from django.urls import path
from .views import *
app_name = 'Booking'
urlpatterns = [
    path('flights/', search_flights, name='search_flights'),
]

from django.urls import path
from . import views

app_name = 'Booking'

urlpatterns = [
    path('', views.flights_view, name='Home'),
    path('flights/', views.search_flights, name='search_flights'),
    
]

from django.urls import path
from . import views

urlpatterns = [
     path('', views.Tour_planner, name= 'Tour_planner' ),
     path('itinerary', views.itinerary, name= 'itineary'),
]

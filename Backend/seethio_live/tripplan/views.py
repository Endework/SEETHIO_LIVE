# from django.shortcuts import render
from django.shortcuts import render

def Tour_planner(request):
    return render(request, 'Tour_planner.html')

def itinerary(request):
    return render(request, 'itinerary.html')

# Create your views here.

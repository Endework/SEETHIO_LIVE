
# flight_search/forms.py
from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=3)
    destination = forms.CharField(max_length=3)
    departure_date = forms.DateField()

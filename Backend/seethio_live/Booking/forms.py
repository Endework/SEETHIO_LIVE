
# flight_search/forms.py
from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=3)
    destination = forms.CharField(max_length=3)
    departure_date = forms.DateField()

# forms.py

class HotelSearchForm(forms.Form):
    destination = forms.CharField(max_length=255)
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()
    # Add other relevant fields

from django import forms

from userauthentication.models import User


#forms for flight by ogo

class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    departure_date = forms.DateField()
    # Add other relevant fields as needed

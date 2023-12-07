from django.shortcuts import render
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from amadeus import Client, ResponseError
from .forms import FlightSearchForm

def flights_view(request):
    return render(request, 'Html/Flight/flight.html')

def search_flights(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            # Perform Amadeus API request using the form data
            # Update the view logic based on Amadeus API response
            # Save relevant data to the Flight model
            # Render the results to the user
            return render(request, 'flight_search/results.html', {'flights': flights})
    else:
        form = FlightSearchForm()

    return render(request, 'flight_search/search_flights.html', {'form': form})


# def search_flights(request):
#     if request.method == 'POST':
#         form = FlightSearchForm(request.POST)
#         if form.is_valid():
#             # Retrieve data from the form
#             origin = form.cleaned_data['origin']
#             destination = form.cleaned_data['destination']
#             departure_date = form.cleaned_data['departure_date']

#             # Initialize the Amadeus client with your API key
#             amadeus = Client(
#                 client_id='settings.AMADEUS_API_KEY,',
#                 client_secret='settings.AMADEUS_API_SECRET',
#                 hostname='test.api.amadeus.com'  # Change to 'api.amadeus.com' for production
#             )

#             try:
#                 # Make a request to the Amadeus Flight Offers Search API
#                 response = amadeus.shopping.flight_offers_search.get(
#                     originLocationCode=origin,
#                     destinationLocationCode=destination,
#                     departureDate=departure_date,
#                     adults=1  # Adjust parameters as needed
#                 )

#                 # Process the API response and store it in the database or return as JSON
#                 # (You'll need to adapt this based on the actual Amadeus API response structure and your model)

#                 # For simplicity, just return the Amadeus API response as JSON
#                 return JsonResponse(response.data)

#             except ResponseError as e:
#                 # Handle Amadeus API response errors
#                 return JsonResponse({'error': str(e)})

#     else:
#         form = FlightSearchForm()
#     return render(request, 'search_flights.html', {'form': form})




from flask import Flask, request, jsonify
from trip_itinerary_generator import TripItineraryGenerator

app = Flask(__name__)

itinerary_generator = TripItineraryGenerator()

@app.route('/')
def home():
    return 'Welcome to Seethio Trip Itinerary API'

@app.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    data = request.get_json()
    location = data.get('location')
    trip_length = data.get('trip_length')
    trip_interest = data.get('trip_interest')

    if not location or not trip_length or not trip_interest:
        return jsonify({"error": "Missing required data."}), 400

    itinerary = itinerary_generator.generate_itinerary(location, trip_length, trip_interest)

    return jsonify(itinerary)

if __name__ == '__main__':
    app.run(debug=True)

import random  

class TripItineraryGenerator:
    def __init__(self):
        self.destinations = ['Addis Ababa', 'Mekele', 'Axum', 'Harar', 'Bahirdar', 'Lalibela', 'Adigrat']
        
        self.trip_interests = ['Sights & Landmarks', 'History', 'Nature & Wildlife', 'Adventure']

        self.trip_interests_mapping = {
                "Addis Ababa": {
                    'Sights & Landmarks': ['Explore the Danakil Depression in 6 Days', 'Day trip to Adadi Mariyam and Melka kunture', 'Full Day Private Tour of to Meskel Square', 'Visit The Mausoleum of Menelik II', 'Full Day Tour of Yekatit 12 Martyrs Square with Hotel Pickup and Dropoff', 'Addis Ababa Guided City Tour With Airport & Hotel Pick Up', 'Visit Karls Square'],
                    'History': ['Discover Red Terror Martyrs Memorial Museum', 'Full Day Tour of National Museum of Ethiopia with Hotel Pickup and Dropoff', 'Addis Ababa Ethnological Museum Tour', 'Visit to Entoto Maryam Church', 'Learn about nature and Ethiopian history and culture at Unity Park Addis Ababa with Hotel Pickup & Dropoff Included', 'Addis Ababa City Tour to Menelik palace', 'Discover the Specialty PanAfrican museum located in Addis Ababas historic Arada district Expect a truly one of a kind memorable experience', 'Addis Ababa Guided Museum Tour With Hotel Pick Up', 'See Zoma Museum'],
                    'Nature & Wildlife': ['Mount Entoto Full Day Tour with Hotel Pickup and Dropoff', 'Day Trip To Menagesha Suba Forest', 'Day Trip To Gullele Botanical Garden'],
                    'Adventure': ['Horseriding experience in the hills surrounding Addis Ababa Come to the ranch to explore nature in its best on trails through the forest learn how to ride or simply get away from the city for a bit Nestled in the Sululta hills 4 kilometers above the capital city with 5 hectares of land', 'Some outdoor activities with Abyssinia Balloon rides', 'Adventure Theme Park at Kuriftu Resort Entoto', 'Addis Ababa City Danakil Depression Tours', 'Rent a car and drive to Portuguese Bridge (110km from Addis Ababa)', 'Ethio North Trekking Come and discover the thrills of Ethiopia with Bale Mountains'],
                },
                "Mekele": {
                    'Sights & Landmarks': ['Go see The Martyrs Memorial Monument'],
                    'History': ['Visit to Emperor Yohannes IV Palace'],
                    'Nature & Wildlife': ['Two Days Tour of Gheralta Rock', 'Four (4) Days tour of Lake Assale'],
                    'Adventure': ['Ethio Cycling Tour'],
                },
                "Axum": {
                    'Sights & Landmarks': ['Explore North Ethiopia Discover King Ezanas Inscription', 'Explore North Ethiopia Visit Church of Our Lady Mary of Zion', 'Discover The Tombs of Kings Kaleb and Gebre Meskal'],
                    'History': ['Day Trip in Axum to discover the remains of once powerful royal capital contain impressive tombs and stelae Ruins of Aksum', 'Explore Church of Our Lady Mary of Zion rumored to be the hiding place of the biblical Lost Ark', 'Discover Queen of Shebas Palace in Axum tall carved obelisks relics of the ancient Kingdom of Aksum'],
                    'Nature & Wildlife': ['Trip interest not found for this location'],
                    'Adventure': ['15 Days trekking To Simen Mountains', 'Discover Ezana Park'],
                },
                "Harar": {
                    'Sights & Landmarks': ['Harrar tour to see Harar Jegol Wall'],
                    'History': ['Explore Casa Museo di Rimbaud', 'Visit Harar Museum Eastern Ethiopia'],
                    'Nature & Wildlife': ['Trip interest not found for this location'],
                    'Adventure': ['Trip interest not found for this location'],
                },
                "Bahirdar": {
                    'Sights & Landmarks': ['Visit Monastery of Debre Mariam', 'Visit Azwa Mariam Monastery'],
                    'History': ['Explore Church of Debre Sina Maryam'],
                    'Nature & Wildlife': ['Bahir Dar Tour of Lake Tana', 'Day trip to Blue Nile Falls'],
                    'Adventure': ['Bahir Dar Bike Tour'],
                },
                "Lalibela": {
                    'Sights & Landmarks': ['Lalibela Rock Churches Guided Tour', 'Visit Monastery of Naakuto Laab', 'Visit The Tomb of Adam', 'Visit Bilbala St George Rock Hewn Church', 'Visit Biete Medhane Alem', 'Visit Rock Hewn Churches'],
                    'History': ['Visit The church of Yemrehanna Kristos is one of Ethiopias best preserved late Axumite churches', '3 days tour to Lalibela Asheton Maryam Monastery'],
                    'Nature & Wildlife': ['4 Day Abune Yosef Conservation Area Trekking Tour from Lalibela'],
                    'Adventure': ['Adventure Theme Park at Kuriftu Resort Entoto', '15 Days trekking To Simen Mountains', 'Lalibela Eco Trekking Tours', 'Some outdoor activities with Abyssinia Balloon rides'],
                },
                "Adigrat": {
                    'Sights & Landmarks': ['Trip interest not found for this location'],
                    'History': ['Two Days Trip to learn about Monastery of Debre Damo'],
                    'Nature & Wildlife': ['Trip interest not found for this location'],
                    'Adventure': ['Trip interest not found for this location'],
                }
            }

        self.hotels = {
            "Addis Ababa": ['Sheraton Addis Hotel', 'Heyday Hotel', 'Radisson Hotel', 'Intercontinental Hotel', 'Capital Hotel And Spa', 'Hilton Hotel', 'Hyatt Hotel', 'Ethiopian Skylight'],
            "Mekele": ['Axum Hotel', 'Planet Hotel', 'Atse Yohannes Hotel', 'Moringa Hotel', 'Desta International Hotel', 'Mekelle Hotel', 'Romanat Hotel'],
            "Axum": ['Africa Hotel', 'Armah Hotel', 'Consolar International Hotel', 'Brana Hotel', 'Axum Touring Hotel'],
            "Harar": ['Rewda Waber Harari Cultural Guest House', 'Wonderland Hotel', 'Harar Ras Hotel', 'Heritage Plaza Hotel', 'Winta Hotel', 'Sumeya Hotel'],
            "Bahirdar": ['Teferi Mokonnen Hotel', 'B&B The Annex', 'Delano Hotel & Spa', 'Jacaranda Hotel', 'Addis Amba Hotel', 'Wynn Hotel', 'Blue Nile Resort', 'Rahnile Hotel', 'Water Front Hotel', 'Lakemark Hotel'],
            "Lalibela": ['Ancient Lalibela Hotel', 'Lal Hotel & Spa', 'Merkeza Hotel', 'Top Twelve Hotel', 'Honey Land Hotel', 'Holidays Hotel'],
            "Adigrat": ['Eve Hotel', 'Hohoma Hotel', 'Gebreselassie Hotel', 'Canaan Hotel', 'Agamos Hotel', 'Agoro Lodge']
            }

        self.restaurants = {
            "Addis Ababa": ['Verres en Vers', 'Sichuan Restaurant', 'La Mandoline', 'Villaverde Addis Ababa', '2000 Habesha Cultural Restaurant', 'The Oriental', 'Gusto Restaurant', 'Opium Restaurant', 'Louvre Grand Hotel', 'Dok Restaurant', 'Dashen Traditional Ethiopian Restaurant', 'Effoi Pizza', 'The Kitchen', 'Castelli Restaurant', 'OM Indian Bistro', 'Makush Art Gallery & Italian Restaurant', 'Lucy Lounge & Restaurant', 'Fendika Azmari Bet', 'Five Loaves', 'Kaffa House', 'Bait Al Mandi', 'Kategna Restaurant', 'Sishu', 'Aladdin Restaurant', 'Gazebo Restaurant on the Park', "Cascara Coffee & Cocktails"],
            "Mekele": ['Samiel G/Slasse Gebru Restaurant', 'Beefmn Garden Bar and Restaurant', 'Karibu Kitchen', 'Geza Gerlase # 1', 'Grand Awash 2 Bar & Restaurant', 'Yordanos Restaurant', 'Elaz Coffee', 'Abay Cultural Restaurant', 'Makale Chinese Restaurant', 'Day to Day Traditional Restaurant', 'Natna Spot'],
            "Axum": ['Africa Hotel', 'Central Cafe Pastry and Restaurant', 'AB Cultural Restaurant', 'Abinet Hotel', 'Aksum Classical Restaurant', 'Lucy Cultural Restaurant', 'Lucy Traditional Restaurant', 'Antica Special Cultural Restaurant', 'Kuda Juice & Pizzeria', 'AB Restaurant', 'Yeha Hotel'],
            "Harar": ['Hirut', 'Ras Hotel Restaurant', 'Nadia Ousmail Ahmed', 'Abdulwasi Adus Cafe', 'Fresh Touch Bar & Restaurant'],
            "Bahirdar": ['Bahir Dar Restaurant', 'Lemat Restaurant', 'Wude Coffee'],
            "Lalibela": ['Old Abyssinia Lodge and Restaurant', 'Jerusalem Guest House', 'Roha Hotel Restaurant', 'Mountain View Hotel Bar & Restaurant', 'Lasta Café', 'Terrace Traditional Hall', 'Unique Restaurant', 'Seven Olives Hotel Restaurant', 'Segenet Cafe and Resturant', 'Sora Lodge Lalibela Restaurant', 'Alem Cooking Class Bar and Restaurant', 'Selina Restaurant', 'Maribela Hotel, Restaurant & Lounge', 'Zan-Seyoum Restaurant', 'Fikr Juice House', 'Ben Abeba', 'Kana Restaurant and Bar', 'Tg home style lalibela restaurant', 'Bisrat cafe', 'Panoramic View Hotel', 'Haset restaurant', "Ma'ed Lalibela Restaurant", 'Kana Restuarant and Bar'],
            "Adigrat": ['Geza Gerelase Hotel']
            }

        self.activities = {
            "Addis Ababa": ['Visit to Entoto Maryam Church', 'Addis Ababa Guided City Tour With Airport & Hotel Pick Up', 'Discover Red Terror Martyrs Memorial Museum', 'See Zoma Museum', 'Mount Entoto Full Day Tour with Hotel Pickup and Dropoff', 'Explore the Danakil Depression in 6 Days', 'Full Day Tour of National Museum of Ethiopia with Hotel Pickup and Dropoff', 'Horseriding experience in the hills surrounding Addis Ababa Come to the ranch to explore nature in its best on trails through the forest learn how to ride or simply get away from the city for a bit Nestled in the Sululta hills 4 kilometers above the capital city with 5 hectares of land', 'Learn about nature and Ethiopian history and culture at Unity Park Addis Ababa with Hotel Pickup & Dropoff Included', 'Visit Karls Square', 'Visit The Mausoleum of Menelik II', 'Rent a car and drive to Portuguese Bridge (110km from Addis Ababa)', 'Day Trip To Menagesha Suba Forest', 'Addis Ababa City Danakil Depression Tours', 'Ethio North Trekking Come and discover the thrills of Ethiopia with Bale Mountains', 'Day Trip To Gullele Botanical Garden', 'Addis Ababa Ethnological Museum Tour', 'Addis Ababa City Tour to Menelik palace', 'Day trip to Adadi Mariyam and Melka kunture', 'Addis Ababa Guided Museum Tour With Hotel Pick Up', 'Full Day Tour of Yekatit 12 Martyrs Square with Hotel Pickup and Dropoff', 'Adventure Theme Park at Kuriftu Resort Entoto', 'Full Day Private Tour of to Meskel Square', 'Discover the Specialty PanAfrican museum located in Addis Ababas historic Arada district Expect a truly one of a kind memorable experience', 'Some outdoor activities with Abyssinia Balloon rides'],
            "Mekele": ['Four (4) Days tour of Lake Assale', 'Ethio Cycling Tour', 'Two Days Tour of Gheralta Rock', 'Go see The Martyrs Memorial Monument', 'Visit to Emperor Yohannes IV Palace'],
            "Axum": ['Discover Ezana Park', 'Explore Church of Our Lady Mary of Zion rumored to be the hiding place of the biblical "Lost Ark', 'Day Trip in Axum to discover the remains of once powerful royal capital contain impressive tombs and stelae Ruins of Aksum', 'Explore North Ethiopia Discover King Ezanas Inscription', 'Discover The Tombs of Kings Kaleb and Gebre Meskal', '15 Days trekking To Simen Mountains', 'Explore North Ethiopia Visit Church of Our Lady Mary of Zion', 'Discover Queen of Shebas Palace in Axum tall carved obelisks relics of the ancient Kingdom of Aksum'],
            "Harar": ['Explore Casa Museo di Rimbaud', 'Visit Harar Museum Eastern Ethiopia', 'Visit Joel Harar Tour', 'Lalibela Omo Valley and Harrar tour to see Harar Jegol Wall'],
            "Bahirdar": ['Bahir Dar Bike Tour', 'Explore Church of Debre Sina Maryam', 'Visit Monastery of Debre Mariam', 'Day trip to Bahir dar To visit lake tana monasteries and Blue Nile Falls', 'Bahir Dar Tour of Lake Tana', 'Visit Azwa Mariam Monastery'],
            "Lalibela": ['3 days tour to Lalibela Asheton Maryam Monastery', 'Visit Monastery of Na’akuto La’ab', 'Hiking & Camping at Lalibela Rock Churches Guided Tour', 'Visit Rock Hewn Churches', 'Visit The church of Yemrehanna Kristos is one of Ethiopias best preserved late Axumite churches', 'Visit Biete Medhane Alem', 'Lalibela Eco Trekking Tours', '4 Day Abune Yosef Conservation Area Trekking Tour from Lalibela', 'Visit Bilbala St George Rock Hewn Church', 'Lalibela Rock Churches Guided Tour', 'Visit The Tomb of Adam'],
            "Adigrat": ['Two Days Trip to learn about Monastery of Debre Damo']
            }

        

    def generate_itinerary(self, location, trip_length, trip_interest):
        if location not in self.destinations:
            return "Location not found in destinations."

        if trip_interest not in self.trip_interests:
            return "Trip interest not found."

        location_interest_mapping = self.trip_interests_mapping.get(location)

        if not location_interest_mapping:
            return "No activity recommendations for this location."

        activities_for_interest = location_interest_mapping.get(trip_interest)

        if not activities_for_interest:
            return "No activities found for this location and interest."

        location_index = self.destinations.index(location)

        # Sets to keep track of chosen hotels, restaurants, and activities
        chosen_hotels = set()
        chosen_restaurants = set()
        chosen_activities = set()

        itinerary = []

        for day in range(1, trip_length + 1):
            destination = location

            # To choose a hotel that hasn't been chosen before
            hotel = random.choice([h for h in self.hotels[location] if h not in chosen_hotels])
            chosen_hotels.add(hotel)

            # To choose a restaurant that hasn't been chosen before
            restaurant = random.choice([r for r in self.restaurants[location] if r not in chosen_restaurants])
            chosen_restaurants.add(restaurant)

            # To choose an activity from the mapped activities
            if activities_for_interest:
                activity = random.choice(activities_for_interest)
                chosen_activities.add(activity)
            else:
                activity = "No activities available for this interest."

            day_itinerary = {
                "Day": day,
                "Destination": destination,
                "Hotel": hotel,
                "Restaurant": restaurant,
                "Activity": activity
            }

            itinerary.append(day_itinerary)

        return itinerary
def recommend_activity(activities_matrix, cosine_similarities, trip_interest, chosen_activities, activities_for_location, trip_interests_mapping):
    interest_index = trip_interests.index(trip_interest) 

    # Calculate location similarity
    location_similarity = cosine_similarities[interest_index]
    location_sorted_indices = location_similarity.argsort()[::-1]

    # Calculate interest similarity
    interest_similarity = cosine_similarities[:, interest_index]
    interest_sorted_indices = interest_similarity.argsort()[::-1]

    for index in location_sorted_indices:
        activity = activities_for_location[index]
        if activity not in chosen_activities:
            if index in interest_sorted_indices:
                return index

    return -1

# User input
location = "Lalibela"  
trip_length = 3  
trip_interest = "Adventure"  

# Create an instance of the TripItineraryGenerator
itinerary_generator = TripItineraryGenerator()

# Generate the itinerary
itinerary = itinerary_generator.generate_itinerary(location, trip_length, trip_interest)

# Print the itinerary
print(f"🌍 Welcome to your exciting trip to {location}! 🌍")
print("Here's your personalized travel itinerary:")
print("-" * 40)

for day in itinerary:
    print(f"🗓️ Day {day['Day']} - {day['Destination']} Adventures:")
    print(f"🏨 Hotel: Stay at {day['Hotel']}")
    print(f"🍽️ Lunch: Eat at {day['Restaurant']}")
    print(f"🎉 Activity: {day['Activity']}")
    print(f"🍽️ Dinner: Have dinner at {day['Restaurant']}")
    print("-" * 40)

print("Enjoy your journey and make wonderful memories! 😊")

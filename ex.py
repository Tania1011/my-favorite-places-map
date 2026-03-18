"""
SIMPLE EXERCISE: My Favorite Places Map

A beginner-friendly introduction to OOP with maps!

OBJECTIVES:
1. Learn the 4 pillars of OOP with simple examples
2. Create a map of your favorite places
3. No complex APIs - we'll use simple sample data

WHAT YOU'LL LEARN:
- Encapsulation: Keeping data and methods together
- Abstraction: Hiding complex details
- Inheritance: Creating specialized classes
- Polymorphism: Same method, different behavior

BEFORE YOU BEGIN:
Install required package:
    pip install folium
"""

import folium
import webbrowser
import math



# ============================================================================
# PART 1: BASE CLASS - Learning Encapsulation
# ============================================================================

class Place:
    """
    A simple place with a name and coordinates.
    
    ENCAPSULATION: This class bundles together:
    - Data: name, latitude, longitude
    - Methods: get_info(), distance_to()
    """
    
    def __init__(self, name, latitude, longitude):
        # Attributes (data)
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def get_info(self):
        """Return basic information about this place"""
        return f"{self.name} ({self.latitude}, {self.longitude})"
    
    def distance_to(self, other_place):
        """
        Calculate distance to another place in kilometers
        This is a simplified formula for beginners
        """
        # Difference in latitude and longitude
        lat_diff = self.latitude - other_place.latitude
        lon_diff = self.longitude - other_place.longitude
        
        # Simple Euclidean distance (good enough for learning)
        # 1 degree ≈ 111 km
        distance_km = math.sqrt(lat_diff**2 + lon_diff**2) * 111
        
        return round(distance_km, 2)
    
    def get_marker_color(self):
        """Default marker color - will be overridden by child classes"""
        return "blue"
    
    def get_popup_text(self):
        """Text to show when clicking on marker"""
        return f"<b>{self.name}</b><br>Click for more info!"


# ============================================================================
# PART 2: YOUR TURN! - Practice Inheritance and Polymorphism
# 
# TODO: Create three specialized types of places
# Each should INHERIT from Place and add its own features
# ============================================================================
# CHILD CLASSES

class Restaurant(Place):
    """
    TODO: Create a Restaurant class that inherits from Place
    
    HINTS:
    1. Use super().__init__() to call the parent constructor
    2. Add a new attribute: food_type (e.g., "Italian", "Chinese")
    3. Override get_popup_text() to show restaurant info
    4. Override get_marker_color() - use "red" for restaurants
    """
    
    def __init__(self, name, latitude, longitude, food_type):
        # TODO: Call the parent constructor
        super().__init__(name, latitude, longitude)
        # TODO: Store food_type as an attribute
        self.food_type = food_type
    
    # TODO: Override get_popup_text()
    # Should return: "<b>RESTAURANT: name</b><br>Food: food_type"
    def get_popup_text(self):
        return f"<b>RESTAURANT: {self.name}</b><br>Food: {self.food_type}"
    
    # TODO: Override get_marker_color()
    def get_marker_color(self):
        return "red"
    # Should return: "red"


class Park(Place):
    """
    TODO: Create a Park class that inherits from Place
    
    HINTS:
    1. Add a new attribute: has_playground (True/False)
    2. Override get_popup_text() to show park info
    3. Override get_marker_color() - use "green" for parks
    """
    
    def __init__(self, name, latitude, longitude, has_playground):
        # TODO: Call the parent constructor
        super().__init__(name, latitude, longitude)
        # TODO: Store has_playground as an attribute
        self.has_playground = has_playground  

    #  pass
    
    # TODO: Override get_popup_text()
    # Should include playground info: "Playground: Yes/No"
    def get_popup_text(self):
        if self.has_playground:
            playground = "Yes"         
        else:
            playground = "No"
        return f"<b>PARK: {self.name}</b><br>Playground: {playground}"
    
    
    # TODO: Override get_marker_color()
    # Should return: "green"
    def get_marker_color(self):
        return "green"


class Museum(Place):
    """
    TODO: Create a Museum class that inherits from Place
    
    HINTS:
    1. Add a new attribute: entry_fee (in euros)
    2. Override get_popup_text() to show museum info
    3. Override get_marker_color() - use "purple" for museums
    """
    
    def __init__(self, name, latitude, longitude, entry_fee):
        # TODO: Call the parent constructor
        super().__init__(name, latitude, longitude)
        # TODO: Store entry_fee as an attribute
        self.entry_fee = entry_fee
        # pass
    
    # TODO: Override get_popup_text()
    # Should include: "Entry: €X"
    def get_popup_text(self):
        return f"<b>MUSEUM: {self.name}</b><br>Entry: €{self.entry_fee}"
    
    
    # TODO: Override get_marker_color()
    # Should return: "purple"
    def get_marker_color(self):
        return "purple"


#  BONUS CHALLENGE 1: Add a new place type
# Create a "Cafe" class that inherits from Restaurant
# - Add a new attribute: has_wifi (True/False)
# - Override get_popup_text() to include wifi info   

class Cafe (Restaurant):

    def __init__(self, name, latitude, longitude, food_type="Cafe", has_wifi=False):
        super().__init__(name, latitude, longitude, food_type)  
        self.has_wifi = has_wifi

    def get_popup_text(self):
        if self.has_wifi:
            wifi_text = "Yes"
        else:
            wifi_text = "No"
        return  f"<b>CAFE: {self.name}</b><br>Food: {self.food_type}<br>WI-FI: {wifi_text}"


    def get_marker_color(self):
        return "orange"



# ============================================================================
# PART 3: MAP CLASS - More Encapsulation
# ============================================================================

class MyMap:
    """
    This class ENCAPSULATES all map-related functionality
    """
    
    def __init__(self, city, zoom=12, tiles="Stamen Terrain"):
        """Create a new map centered on a city"""
        self.city = city
        self.places = []  # List to store all our places
        
        # Map centers for some cities
        centers = {
            "Paris": [48.8566, 2.3522],
            "London": [51.5074, -0.1278],
            "New York": [40.7128, -74.0060],
            "Tokyo": [35.6762, 139.6503]
        }
        
        # Get center coordinates or use default
        if city in centers:
            center = centers[city]
        else:
            center = [0, 0]  # Default to (0,0)
            print(f"Warning: {city} not in our list, using (0,0)")
        
        # Create the map with safe tiles
        self.map = folium.Map(location=center, zoom_start=zoom, tiles=tiles)
        print(f"🗺️  Created map of {city} using '{tiles}' tiles")
    
    def add_place(self, place):
        """
        Add a place to the map
        
        This demonstrates POLYMORPHISM - the same method works
        for any type of Place (Restaurant, Park, Museum)!
        """
        # Add to our list
        self.places.append(place)
        
        # Create a marker on the map
        folium.Marker(
            location=[place.latitude, place.longitude],
            popup=folium.Popup(place.get_popup_text(), max_width=300),  # Different for each place type! # ensures full text is visible,max_width ensures the popup doesn’t get cut off.
            tooltip=place.name,
            icon=folium.Icon(color=place.get_marker_color())  # Different colors!
        ).add_to(self.map)
        
        print(f"  ✅ Added: {place.name}")


    
    def show_distances(self):
        """
        Show distances between all places
        """
        if len(self.places) < 2:
            print("Add at least 2 places to see distances")
            return
        
        print(f"\n📏 Distances in {self.city}:")
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                place1 = self.places[i]
                place2 = self.places[j]
                dist = place1.distance_to(place2)
                print(f"  {place1.name} → {place2.name}: {dist} km")

    
    def save(self, filename="my_map.html"):
        """Save the map to an HTML file"""
        self.map.save(filename)
        print(f"\n💾 Map saved as '{filename}'")
        return filename
    
# BONUS CHALLENGE 2: Find the closest places
# Write a function that finds the two closest places on your map
    
    def find_closest_places(self):
        if len(self.places) < 2:
            print("Not enough places") #  at least 2 places needed to compare
            return

        min_distance = float('inf')         #Start with ∞
        closest_pair = (None, None)         #Stores the best (closest) two places-initially empty

        for i in range(len(self.places)):  #compare place 1 with 2, place 1 with 3, place2 with place 3
            for j in range(i + 1, len(self.places)):
                p1 = self.places[i]
                p2 = self.places[j]         #picking a pair to compare
                dist = p1.distance_to(p2)   #calculate distance 
                if dist < min_distance:
                    min_distance = dist     #Save new minimum distance
                    closest_pair = (p1, p2) #Save the pair 

        p1, p2 = closest_pair               #Unpack the best pair
        print(f"\n🏆 Closest places:")
        print(f"{p1.name} ↔ {p2.name}")
        print(f"Distance: {min_distance} km")


# ============================================================================
# PART 4: CREATE YOUR MAP!
# 
# TODO: Fill in the missing code to create your own map
# ============================================================================

def create_my_places():
    """
    Create a list of your favorite places
    
    TODO: Replace these with your own favorite places!
    """
    places = []
    
    # TODO: Add at least 2 restaurants
    # Example: Restaurant("Pizza Hut", 40.7128, -74.0060, "Italian")
    # restaurants = [...]
    
     # Restaurants
    places.append(Restaurant("Sushi Place", 49.1666, -123.1336, "Japanese"))
    places.append(Restaurant("Italian Bistro", 49.1700, -123.1400, "Italian"))
    places.append(Restaurant("Taco Spot", 49.1680, -123.1300, "Mexican"))
    places.append(Restaurant("Burger Joint", 49.1690, -123.1320, "American"))
    places.append(Restaurant("Vegan Cafe", 49.1670, -123.1280, "Vegan"))

    
    # TODO: Add at least 2 parks
    # parks = [...]
    # Parks
    places.append(Park("Minoru Park", 49.1667, -123.1403, True))
    places.append(Park("Garden City Park", 49.1750, -123.1230, False))
    places.append(Park("West Richmond Park", 49.1685, -123.1380, True))
    places.append(Park("Steveston Park", 49.1650, -123.1250, False))
    places.append(Park("Thompson Community Park", 49.1710, -123.1300, True))
    
    # TODO: Add at least 1 museum
    # museums = [...]
    # Museums
    places.append(Museum("Richmond Art Gallery", 49.1700, -123.1350, 5))
    places.append(Museum("Richmond Museum", 49.1705, -123.1360, 10))
    places.append(Museum("Richmond Nature House", 49.1680, -123.1703, 0) )

    
    # Combine all places
    # places.extend(restaurants)
    # places.extend(parks)
    # places.extend(museums)
    
    return places


def main():
    """
    Main function - this is where your program starts!
    """
    print("=" * 50)
    print("🗺️  MY FAVORITE PLACES MAP")
    print("=" * 50)
    print("\nThis program demonstrates the 4 pillars of OOP:")
    print("1. ENCAPSULATION: Place class bundles data + methods")
    print("2. INHERITANCE: Restaurant, Park, Museum inherit from Place")
    print("3. POLYMORPHISM: get_popup_text() works differently for each")
    print("4. ABSTRACTION: MyMap hides map complexity")
    print("\n" + "-" * 50)
    
    # TODO 1: Choose a city
    # Available: Paris, London, New York, Tokyo
    my_city = "New York"  # Change this to your favorite city
    
    # Create a map
    # mymap = MyMap(my_city)
    # mymap = MyMap("New York", tiles="CartoDB positron")
    # mymap = MyMap("New York", tiles="CartoDB dark_matter")
    mymap = MyMap("New York", tiles="OpenStreetMap")
    
    # TODO 2: Get your places
    # my_places = create_my_places()

    # For now, let's use some sample places (replace with your own!)
    print("\n📝 Using sample places (TODO: Replace with your favorites!)")
    
    # Create some sample places
    # eiffel_tower = Place("Eiffel Tower", 48.8584, 2.2945)
    # louvre = Museum("Louvre Museum", 48.8606, 2.3376, 17)
    # cafe = Restaurant("Cafe Paris", 48.8566, 2.3522, "French")
    # park = Park("Luxembourg Garden", 48.8462, 2.3372, True)

    # Museums
    empire_state_building = Museum ("Empire State Building", 40.7484, -73.9857, 100)
    one_world_trade_center= Museum ("One World Trade Center", 40.7127, -74.0134, 60)
     # Parks
    central_park = Park("Central Park", 40.7851, -73.9683, True)
    bryant_park = Park ("Bryant Park", 40.7536, -73.9832, 0)
    # Restaurants
    katz_restaurant = Restaurant("Katz's Delicatessen", 40.7223, -73.9874, "American")
    balthazar_restaurant=Restaurant("Balthazar", 40.7226, -73.9982, "French")
    nobu_restaurant=Restaurant("Nobu Downtown", 40.7147, -74.0070, "Japanese")
    # Cafe
    blue_cafe= Cafe ("Blue Bottle Coffee", 40.7283, -73.9946, "Cafe", False)




    
    # TODO 3: Add all places to the map
    mymap.add_place(empire_state_building)
    mymap.add_place(one_world_trade_center)
    mymap.add_place(central_park)
    mymap.add_place(bryant_park)
    mymap.add_place(katz_restaurant)
    mymap.add_place(balthazar_restaurant)
    mymap.add_place(nobu_restaurant)
    mymap.add_place(blue_cafe)

    
    # TODO 4: Show distances between places
    mymap.show_distances()

    # TODO: challenge 2
    mymap.find_closest_places()

    
    # TODO 5: Save the map
    filename = mymap.save("my_favorite_places.html")
    
    # Open in browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)
    
    print("\n" + "=" * 50)
    print("✅ EXERCISE COMPLETE!")
    print("=" * 50)
    print("\nREFLECTION QUESTIONS:")
    print("1. How did Restaurant, Park, and Museum INHERIT from Place?")
    print("2. How is POLYMORPHISM shown when adding places to the map?")
    print("3. What data and methods are ENCAPSULATED in the Place class?")
    print("4. What complexity does the MyMap class ABSTRACT away?")
    print("\n🎯 BONUS: Try adding your own real favorite places!")


# ============================================================================
# BONUS: Challenge yourself!
# ============================================================================

"""
BONUS CHALLENGE 1: Add a new place type
Create a "Cafe" class that inherits from Restaurant
- Add a new attribute: has_wifi (True/False)
- Override get_popup_text() to include wifi info

BONUS CHALLENGE 2: Find the closest places
Write a function that finds the two closest places on your map

BONUS CHALLENGE 3: Add markers for YOUR city
Look up coordinates for your favorite places in YOUR city
Use Google Maps to find coordinates (right-click on a place)
"""


if __name__ == "__main__":
    main()
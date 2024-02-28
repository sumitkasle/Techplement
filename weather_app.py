import requests
import time
from database import connect_to_database, create_tables, add_to_favorites, get_favorite_cities


API_KEY = "7fee53726aa646c3be1120110242702"
BASE_URL = "http://api.weatherapi.com/v1/{}"

favorite_cities = []

def get_weather(city):
    try:
        url = BASE_URL.format("current.json")
        params = {
            "key": API_KEY,
            "q": city
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather_data = {
            "City": data["location"]["name"],
            "Temperature": data["current"]["temp_c"],
            "Weather": data["current"]["condition"]["text"]
        }
        return weather_data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    except KeyError as e:
        print("Unexpected response format:", e)
        return None

def print_weather(weather_data):
    if weather_data:
        print("Weather in {}: ".format(weather_data["City"]))
        print("Temperature: {}°C".format(weather_data["Temperature"]))
        print("Description: {}".format(weather_data["Weather"]))
    else:
        print("Error fetching weather data.")

def add_city(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} already exists in favorites.")

def remove_city(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} not found in favorites.")

def view_favorites():
    if favorite_cities:
        print("Favorite Cities:")
        for city in favorite_cities:
            print("-", city)
        while True:
            inner_choice = input("Enter your choice (1 for searching weather of favorite cities, 2 to exit): ")
            if inner_choice == "1":
                city = input("Enter city name: ")
                weather_data = get_weather(city)
                print_weather(weather_data)
            elif inner_choice == "2":
                break
            else:
                print("Invalid choice.")
    else:
        print("No favorite cities added yet.")

def main():
    
    conn = connect_to_database()
    if conn is None:
        return
    
    create_tables(conn)    
    
    while True:
        print("\nOptions:")
        print("1. Check Weather by City")
        print("2. Add City to Favorites")
        print("3. Remove City from Favorites")
        print("4. View Favorite Cities")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_data = get_weather(city)
            print_weather(weather_data)
        elif choice == "2":
            city = input("Enter city name to add to favorites: ")
            add_city(city)
        elif choice == "3":
            city = input("Enter city name to remove from favorites: ")
            remove_city(city)
        elif choice == "4":
            view_favorites()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    conn.close()
    print("Database connection closed")
    
if __name__ == "__main__":
    main()

import datetime as dt
import time
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "7b9d1c175dcb422a6f78203aab2aa8ab"

# Global variable for the favorite list of cities
favorite_cities = []

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = round(kelvin - 273.15, 2)
    fahrenheit = round(celsius * (9/5) + 32, 2)
    return celsius, fahrenheit

def check_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url).json()

    if response['cod'] == '404':
        print(f"City not found: {city}, Please check the name of entered City.")
    else:
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        wind_speed = response['wind']['speed']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        
        
        print(f"\n\t************ Weather information of {city} City ************")
        print(f"\tTemperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit}°F")
        print(f"\tTemperature in {city} feels_like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit}°F")
        print(f"\tHumidity in {city}: {humidity}%")
        print(f"\tWind speed in {city}: {wind_speed}m/s")
        print(f"\tGeneral Weather in {city}: {description}")
        print(f"\n\t*************** ////////////////\\\\\\\\\\\\\\\\\\\\\\ ***************")


def add_to_favorite(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        print(f"{city} added to the favorite list.")
    else:   
        print(f"{city} is already in the favorite list.")

def remove_from_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from the favorite list.")
    else:
        print(f"{city} is not in the favorite list.")

def display_favorite_list():
    print("\n*******  Favorite Cities  *******")
    for city in favorite_cities:
        print(city)

def auto_refresh(interval_seconds):
    # Check if there are favourite cities.
    if favorite_cities:
        allow = True
        try:
            while allow:
                for city in favorite_cities:
                    print(f"\n******** Weather information for {city} ********")
                    check_weather(city)
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("Program Closed.")
    else:
        print("Please Add cities to the favourite cities.")
# Example usage:
try:
    while True:
        print("\n\t---------Welcome to WEATHERMATE!---------")
        print("\n**Please select an option from the given menu**")
        print("Menu:")
        print("1. Check Weather by City")
        print("2. Add to Favorite List")
        print("3. Remove from Favorite List")
        print("4. Display Favorite List")
        print("5. Auto Refresh Favorite List")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            city = input("Enter the city name: ")
            check_weather(city)
        elif choice == '2':
            city = input("Enter the city name to add to the favorite list: ")
            add_to_favorite(city)
        elif choice == '3':
            city = input("Enter the city name to remove from the favorite list: ")
            remove_from_favorite(city)
        elif choice == '4':
            display_favorite_list()
        elif choice == '5':
            interval_seconds = int(input("Enter auto-refresh interval in seconds (15-30): "))
            auto_refresh(interval_seconds)
        elif choice == '6':
            print("You have chosen to exit the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
except KeyboardInterrupt:
    print("Program Closed")
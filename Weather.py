import requests
import sys

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    print(f"Fetching weather for {location}...")

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        city_name = data.get('name')
        weather_conditions = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        
        print("\n--- Current Weather ---")
        print(f"Location: {city_name}")
        print(f"Conditions: {weather_conditions.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print("-----------------------")

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("\nError: City not found. Please check the spelling and try again.")
        elif response.status_code == 401:
            print("\nError: Invalid API Key. Please check your API key in the script.")
        else:
            print(f"\nAn HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"\nAn error occurred (check your internet connection): {err}")
    except KeyError:
        print("\nError: Could not parse weather data. The API response may have changed.")
    except Exception as err:
        print(f"\nAn unexpected error occurred: {err}")


def main():
    API_KEY = "84e2a11546d199d53ffe2e2d636acba8"
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Error: Please set your API_KEY in the 'weather_app.py' script.")
        sys.exit(1)

    print("--- Basic Weather App ---")
    
    while True:
        location = input("Enter a city name or ZIP code (or 'q' to quit): ").strip()
        
        if location.lower() == 'q':
            print("Goodbye!")
            break
            
        if not location:
            print("Please enter a location.")
            continue
        
        get_weather(API_KEY, location)
        print("\n")

if __name__ == "__main__":
    main()
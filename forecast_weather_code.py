import requests

class WeatherCLIApp:
    def __init__(self):
        self.api_key = "cf24696c80cb3142f835d5558e369035"  # Replace with your OpenWeatherMap API key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location: str):
        if not location:
            print("Please enter a location!")
            return None
        
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                return data
            elif response.status_code == 401:
                print("Invalid API key! Please check your API key.")
            elif response.status_code == 404:
                print("Location not found! Please try again.")
            else:
                print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {str(e)}")
        return None

    def display_weather(self, data):
        city_name = data["name"]
        country = data["sys"].get("country", "N/A")
        temp = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = round(data["wind"]["speed"] * 3.6)  # Convert m/s to km/h
        description = data["weather"][0]["description"].capitalize()
        cloudiness = data["clouds"]["all"]

        print("\n==============================")
        print(f"Weather Report for {city_name}, {country}")
        print("==============================")
        print(f"Temperature : {temp} °C")
        print(f"Description : {description}")
        print(f"Humidity     : {humidity}%")
        print(f"Wind Speed  : {wind_speed} km/h")
        print(f"Pressure     : {pressure} hPa")
        print(f"Cloudiness  : {cloudiness}%")
        print("==============================\n")

    def run(self):
        print("======================================")
        print("Weather Forecast App - Elsayed Bondok")
        print("======================================")
        print("Type 'exit' to quit the program.\n")

        while True:
            location = input("Enter a location: ").strip()
            if location.lower() == "exit":
                print("Exiting the program. Goodbye!")
                break

            data = self.get_weather(location)
            if data:
                self.display_weather(data)

def main():
    app = WeatherCLIApp()
    app.run()

if __name__ == "__main__":
    main()
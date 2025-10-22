import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast - Elsayed Bondok ")
        self.root.geometry("420x540")
        self.root.resizable(False, False)

        # API Config
        self.api_key = "cf24696c80cb3142f835d5558e369035"  # Your Api key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(
            self.root,
            text=" Weather Forecast",
            font=("Arial", 20, "bold"),
            bg="#1E90FF",
            fg="white",
            pady=12
        ).pack(fill="x")

        # Search Frame
        search_frame = tk.Frame(self.root, bg="#F0F0F0")
        search_frame.pack(pady=15)

        tk.Label(search_frame, text="Enter City:", font=("Arial", 12), bg="#F0F0F0").pack(side="left", padx=5)

        self.location_entry = tk.Entry(search_frame, font=("Arial", 12), width=20)
        self.location_entry.pack(side="left", padx=5)
        self.location_entry.bind("<Return>", lambda event: self.get_weather())

        tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.get_weather,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Results Display Frame
        self.result_frame = tk.Frame(self.root, bg="white", relief="ridge", borderwidth=2)
        self.result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.city_label = tk.Label(self.result_frame, text="", font=("Arial", 18, "bold"), bg="white", fg="#333333")
        self.city_label.pack(pady=(10, 5))

        self.temp_label = tk.Label(self.result_frame, text="-- °C", font=("Arial", 42, "bold"), fg="#FF6347", bg="white")
        self.temp_label.pack(pady=5)

        self.desc_label = tk.Label(self.result_frame, text="", font=("Arial", 14, "italic"), bg="white", fg="#555555")
        self.desc_label.pack(pady=5)

        # Separator
        tk.Frame(self.result_frame, height=2, bg="#e0e0e0").pack(fill="x", padx=20, pady=10)

        # Text Widget (for detailed info)
        self.details_text = tk.Text(
            self.result_frame,
            font=("Arial", 12),
            bg="white",
            fg="#333333",
            relief="flat",
            height=8,
            wrap="word",
            spacing1=8,   # Space above each line
            spacing3=8    # Space below each line
        )
        self.details_text.pack(padx=15, pady=(5,15), fill="both", expand=True)
        self.details_text.configure(state="disabled")

    def get_weather(self):
        """Fetch weather information from OpenWeatherMap API."""
        location = self.location_entry.get().strip()
        if not location:
            messagebox.showwarning("Input Error", " Please enter a city name!")
            return

        params = {"q": location, "appid": self.api_key, "units": "metric"}

        try:
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 401:
                messagebox.showerror("API Error", " Invalid API Key! Please check it.")
            elif response.status_code == 404:
                messagebox.showerror("Not Found", " City not found. Try again.")
            else:
                messagebox.showerror("Error", f" Unexpected Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", f" Failed to fetch data:\n{e}")

    def display_weather(self, data):
        """Display all key weather details including precipitation."""
        city = data["name"]
        country = data["sys"]["country"]
        temp = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = round(data["wind"]["speed"] * 3.6)  # Convert m/s to km/h
        description = data["weather"][0]["description"].capitalize()
        clouds = data["clouds"]["all"]

        # --- NEW: Extract precipitation (rain or snow) if available ---
        precipitation = 0.0
        if "rain" in data and "1h" in data["rain"]:
            precipitation = data["rain"]["1h"]
        elif "rain" in data and "3h" in data["rain"]:
            precipitation = data["rain"]["3h"]
        elif "snow" in data and "1h" in data["snow"]:
            precipitation = data["snow"]["1h"]
        elif "snow" in data and "3h" in data["snow"]:
            precipitation = data["snow"]["3h"]
        # If none found, leave at 0 mm (no precipitation)

        # Update top labels
        self.city_label.config(text=f"{city}, {country}")
        self.temp_label.config(text=f"{temp}°C")
        self.desc_label.config(text=description)

        # Display info in block with generous line spacing
        detail_text = (
            f" Humidity: {humidity}%\n"
            f" Wind Speed: {wind_speed} km/h\n"
            f" Pressure: {pressure} hPa\n"
            f" Cloudiness: {clouds}%\n"
            f" Precipitation (last hr): {precipitation} mm"
        )

        self.details_text.configure(state="normal")
        self.details_text.delete("1.0", tk.END)
        self.details_text.insert("1.0", detail_text)
        self.details_text.configure(state="disabled")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
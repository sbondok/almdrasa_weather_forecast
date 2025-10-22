# Weather Forecast Application

Welcome to the **Weather Forecast Application**, a Python-based project built using **Tkinter** for GUI and **OpenWeatherMap API** for real-time weather data. This application is designed to provide users with an intuitive and interactive way to fetch weather details for any city worldwide. The project also includes a command-line interface (CLI) version for lightweight usage.

---
### Note:
- Sorry you have to have API key from [Weather web site](https://openweathermap.org/api)
- You can have a free api key for limited time - just sign up for free.

## Features
### Version 1.0 (GUI)
- Graphical User Interface (GUI) built with **Tkinter**.
- Real-time weather data fetched using the **OpenWeatherMap API**.
- Displays:
  - Current temperature in Celsius.
  - Humidity, wind speed, atmospheric pressure, and cloudiness.
  - Precipitation (rain or snow) details, if available.
- User-friendly error handling for:
  - Invalid city names.
  - Missing API key or network issues.
- Interactive interface with a **Search** button and input field for city names.

### Version 0.1 (CLI)
- Command-Line Interface (CLI) for users who prefer terminal-based interactions.
- Fetches and displays weather details in a structured format.
- Handles input errors gracefully (e.g., invalid city names, API errors).
- Continuous loop for fetching weather data until the user exits.

---

## How It Works
### GUI Workflow
1. The program starts, and the GUI is initialized.
2. The user enters a city name and clicks the **Search** button.
3. The application sends a request to the OpenWeatherMap API.
4. Based on the API response:
   - If successful (HTTP 200): Displays weather information.
   - If the city is not found (HTTP 404): Shows an error popup.
   - If the API key is invalid (HTTP 401): Displays an authentication error.
5. The weather details are displayed in a detailed and user-friendly format.

![GUI Flowchart](https://miro.com/app/board/uXjVJ3neTdY=/?share_link_id=433954352531)

---

### CLI Workflow
1. The program starts and continuously asks the user for a city name.
2. The user enters a city name:
   - If valid: Fetches and displays the weather details.
   - If invalid: Displays an error message.
3. The loop continues until the user types `exit`.

![CLI Flowchart](https://miro.com/app/board/uXjVJ3neTdY=/?share_link_id=433954352531)

---

## Installation and Usage
### Prerequisites
- **Python 3.6+**: Ensure you have Python installed.
- **Tkinter**: This is included in most Python distributions.
- **Requests Library**: Install it using `pip` if not already available:
  ```bash
  pip install requests

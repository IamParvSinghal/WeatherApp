import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import xml.etree.ElementTree as xml_parser
import requests as rq

# Fetch weather details using XML API
def weatherOf(city_name):
    """
    Fetch weather details for a given city using the OpenWeatherMap XML API.

    Args:
        city_name (str): Name of the city to fetch weather information for.

    Returns:
        dict: A dictionary containing weather details such as temperature, humidity, wind direction, etc.,
              or None if the city is not found.
    """
    api_key = "a964d331378c1b746dec6177a6841ee8"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&mode=xml&appid={api_key}"

    response = rq.get(api_url)

    if response.status_code == 404:
        messagebox.showerror("City Not Found", "Please enter a valid city name.")
        return None

    xml_data = xml_parser.fromstring(response.content)

    details = {  # Extract and calculate weather details
        "city": xml_data.find("city").get("name"), 
        "country": xml_data.find("city/country").text, 
        "temperature": (float(xml_data.find("temperature").get("value")) - 273.15) * 9/5 + 32,  # Convert temperature to Fahrenheit
        "feels_like": (float(xml_data.find("feels_like").get("value")) - 273.15) * 9/5 + 32,  # Convert 'feels like' temp to Fahrenheit
        "humidity": xml_data.find("humidity").get("value"),  
        "wind": xml_data.find("wind/direction").get("name"),  
        "pressure": xml_data.find("pressure").get("value"),  
        "temp_min": (float(xml_data.find("temperature").get("min")) - 273.15) * 9/5 + 32,  # Convert min temperature to Fahrenheit
        "temp_max": (float(xml_data.find("temperature").get("max")) - 273.15) * 9/5 + 32,  # Convert max temperature to Fahrenheit
        "description": xml_data.find("weather").get("value"), 
    }

    return details

# Adjust background based on weather condition
def change_background(condition):
    """
    Change the application background image based on the weather condition.

    Args:
        condition (str): Weather condition description (e.g., 'clear sky', 'rain').
    """
    image_map = {
        "clear sky": "WeatherApp/images/clearsky.png",
        "rain": "WeatherApp/images/raining.png",
        "clouds": "WeatherApp/images/cloudy.jpg",
        "haze": "WeatherApp/images/haze.png",
        "mist": "WeatherApp/images/mist.jpg",
    }

    image_file = image_map.get(condition, "WeatherApp/images/default.jpg")
    load_background_image(image_file, app_window.winfo_width(), app_window.winfo_height())

# Load and set the background image
def load_background_image(image_path, width, height):
    """
    Load and resize the background image for the application.

    Args:
        image_path (str): Path to the image file.
        width (int): Width of the application window.
        height (int): Height of the application window.
    """
    img = Image.open(image_path).resize((width, height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)
    bg_label.configure(image=bg_image)
    bg_label.image = bg_image

# Process and display weather details
def display_weather():
    """
    Fetch and display the weather details for the city entered by the user.
    Updates the UI with weather information and adjusts the background image.
    """
    city_name = city_input.get()
    weather_data = weatherOf(city_name)

    if not weather_data:
        return

    condition = weather_data['description'].lower()
    change_background(condition)

    # Move title above the weather information box
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Show weather frame and update details
    weather_frame.place(relx=0.5, rely=0.48, anchor="center", relwidth=0.75, relheight=0.6)
    location_display.config(text=f"{weather_data['city']}, {weather_data['country']}")
    temp_display.config(text=f"Temperature: {weather_data['temperature']:.1f}°F")
    feels_like_display.config(text=f"Feels Like: {weather_data['feels_like']:.1f}°F")
    desc_display.config(text=f"Condition: {weather_data['description']}")
    humidity_display.config(text=f"Humidity: {weather_data['humidity']}%")
    wind_display.config(text=f"Wind: {weather_data['wind']}")
    pressure_display.config(text=f"Pressure: {weather_data['pressure']} hPa")
    temp_min_display.config(text=f"Min Temp: {weather_data['temp_min']:.1f}°F")
    temp_max_display.config(text=f"Max Temp: {weather_data['temp_max']:.1f}°F")

    # Pack labels to show updated details
    location_display.pack(pady=15)
    temp_display.pack()
    feels_like_display.pack()
    desc_display.pack()
    humidity_display.pack()
    wind_display.pack()
    pressure_display.pack()
    temp_min_display.pack()
    temp_max_display.pack()

    # Move search bar and button below the weather information box
    city_input.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.5, relheight=0.07)
    search_button.place(relx=0.5, rely=0.925, anchor="center", relwidth=0.3, relheight=0.07)

# Create the app window
app_window = ttk.Window(themename="superhero")
app_window.title("Weather App")

# Set the dimensions of the square window
window_size = 600

screen_width = app_window.winfo_screenwidth()
screen_height = app_window.winfo_screenheight()

x_coordinate = (screen_width // 2) - (window_size // 2)
y_coordinate = (screen_height // 2) - (window_size // 2)

app_window.geometry(f"{window_size}x{window_size}+{x_coordinate}+{y_coordinate}")

# Background image setup
bg_label = tk.Label(app_window)
bg_label.place(relwidth=1, relheight=1)
load_background_image("WeatherApp/images/default.jpg", app_window.winfo_width(), app_window.winfo_height())

# Title label
title_label = tk.Label(app_window, text="PARV'S WEATHER APP", font=("Times New Roman", 28, "bold"))
title_label.place(relx=0.5, rely=0.35, anchor="center")

# Input field for city name (Initially large and centered)
city_input = ttk.Entry(app_window, font=("Times New Roman", 18))
city_input.insert(0, "Search City")
city_input.bind("<FocusIn>", lambda e: city_input.delete(0, tk.END))
city_input.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.08)

# Search button (Initially large and centered)
search_button = ttk.Button(app_window, text="Get Weather", command=display_weather, bootstyle="primary")
search_button.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.35, relheight=0.075)

# Transparent box for weather details
weather_frame = tk.Frame(app_window, bg="#2b2b2b", bd=2, relief="solid")

# Labels to show weather details
location_display = tk.Label(weather_frame, font=("Times New Roman", 20))
temp_display = tk.Label(weather_frame, font=("Times New Roman", 14))
feels_like_display = tk.Label(weather_frame, font=("Times New Roman", 14))
desc_display = tk.Label(weather_frame, font=("Times New Roman", 14))
humidity_display = tk.Label(weather_frame, font=("Times New Roman", 14))
wind_display = tk.Label(weather_frame, font=("Times New Roman", 14))
pressure_display = tk.Label(weather_frame, font=("Times New Roman", 14))
temp_min_display = tk.Label(weather_frame, font=("Times New Roman", 14))
temp_max_display = tk.Label(weather_frame, font=("Times New Roman", 14))

# Initial hiding of weather details
for widget in [location_display, temp_display, feels_like_display, desc_display, 
               humidity_display, wind_display, pressure_display, temp_min_display, temp_max_display]:
    widget.pack_forget()

app_window.resizable(False, False)
app_window.mainloop()

import tkinter as tk
import ttkbootstrap as ttk  # Import ttkbootstrap for styled widgets
from tkinter import messagebox  # Import messagebox for error handling dialogs
from PIL import Image, ImageTk  # Import PIL for image handling and resizing
import xml.etree.ElementTree as xml_parser  # Import XML parser for processing API responses
import requests as rq  # Import requests for HTTP API requests

# Fetch weather details using XML API
def weatherOf(city_name):
    api_key = "a964d331378c1b746dec6177a6841ee8"  # API key for OpenWeatherMap
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&mode=xml&appid={api_key}"  # Construct API URL

    response = rq.get(api_url)  # Send GET request to the weather API

    if response.status_code == 404:  # Check if the city is not found (404 response code)
        messagebox.showerror("City Not Found", "Please enter a valid city name.")  # Show error dialog
        return None  # Return None to indicate failure

    xml_data = xml_parser.fromstring(response.content)  # Parse XML response content

    details = {  # Extract and calculate weather details
        "city": xml_data.find("city").get("name"),  # Get city name
        "country": xml_data.find("city/country").text,  # Get country code
        "temperature": float(xml_data.find("temperature").get("value")) - 273.15,  # Convert temperature to Celsius
        "feels_like": float(xml_data.find("feels_like").get("value")) - 273.15,  # Convert 'feels like' temp to Celsius
        "humidity": xml_data.find("humidity").get("value"),  # Get humidity percentage
        "wind": xml_data.find("wind/direction").get("name"),  # Get wind direction name
        "pressure": xml_data.find("pressure").get("value"),  # Get pressure value in hPa
        "temp_min": float(xml_data.find("temperature").get("min")) - 273.15,  # Convert min temperature to Celsius
        "temp_max": float(xml_data.find("temperature").get("max")) - 273.15,  # Convert max temperature to Celsius
        "description": xml_data.find("weather").get("value"),  # Get weather condition description
    }

    return details  # Return the extracted weather details

# Adjust background based on weather condition
def change_background(condition):
    image_map = {  # Map weather conditions to corresponding background images
        "clear sky": "Weather-Application-main/images/clearsky.png",
        "rain": "Weather-Application-main/images/raining.png",
        "clouds": "Weather-Application-main/images/cloudy.jpg",
        "haze": "Weather-Application-main/images/haze.png",
        "mist": "Weather-Application-main/images/mist.jpg",
    }

    image_file = image_map.get(condition, "Weather-Application-main/images/default.jpg")  # Get image for the condition or default
    load_background_image(image_file, app_window.winfo_width(), app_window.winfo_height())  # Load and set the background image

def load_background_image(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.LANCZOS)  # Open and resize image to fit window dimensions
    bg_image = ImageTk.PhotoImage(img)  # Convert to PhotoImage for Tkinter compatibility
    bg_label.configure(image=bg_image)  # Set the new image to the background label
    bg_label.image = bg_image  # Keep a reference to avoid garbage collection

# Process and display weather details
def display_weather():
    city_name = city_input.get()  # Get city name from input field
    weather_data = weatherOf(city_name)  # Fetch weather details for the entered city

    if not weather_data:  # Check if weather data retrieval failed
        return  # Exit the function if no data was retrieved

    condition = weather_data['description'].lower()  # Get weather condition in lowercase
    change_background(condition)  # Update background based on weather condition

    title_label.place(relx=0.5, rely=0.1, anchor="center")  # Move the title label above the weather information box

    weather_frame.place(relx=0.5, rely=0.48, anchor="center", relwidth=0.75, relheight=0.6)  # Display the weather frame
    location_display.config(text=f"{weather_data['city']}, {weather_data['country']}")  # Update location display
    temp_display.config(text=f"Temperature: {weather_data['temperature']:.1f}°C")  # Show current temperature
    feels_like_display.config(text=f"Feels Like: {weather_data['feels_like']:.1f}°C")  # Show 'feels like' temperature
    desc_display.config(text=f"Condition: {weather_data['description']}")  # Show weather condition
    humidity_display.config(text=f"Humidity: {weather_data['humidity']}%")  # Display humidity percentage
    wind_display.config(text=f"Wind: {weather_data['wind']}")  # Display wind direction
    pressure_display.config(text=f"Pressure: {weather_data['pressure']} hPa")  # Display atmospheric pressure
    temp_min_display.config(text=f"Min Temp: {weather_data['temp_min']:.1f}°C")  # Show minimum temperature
    temp_max_display.config(text=f"Max Temp: {weather_data['temp_max']:.1f}°C")  # Show maximum temperature

    location_display.pack(pady=15)  # Add padding and pack location label
    temp_display.pack()  # Pack temperature label
    feels_like_display.pack()  # Pack 'feels like' temperature label
    desc_display.pack()  # Pack weather condition label
    humidity_display.pack()  # Pack humidity label
    wind_display.pack()  # Pack wind direction label
    pressure_display.pack()  # Pack pressure label
    temp_min_display.pack()  # Pack minimum temperature label
    temp_max_display.pack()  # Pack maximum temperature label

    city_input.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.5, relheight=0.07)  # Move input field below weather details
    search_button.place(relx=0.5, rely=0.925, anchor="center", relwidth=0.3, relheight=0.07)  # Move search button below input field

app_window = ttk.Window(themename="superhero")  # Create the main application window with 'superhero' theme
app_window.title("Weather App")  # Set the application window title

window_size = 600  # Define the size of the window (square)

screen_width = app_window.winfo_screenwidth()  # Get the width of the user's screen
screen_height = app_window.winfo_screenheight()  # Get the height of the user's screen

x_coordinate = (screen_width // 2) - (window_size // 2)  # Calculate x-coordinate for centering the window
y_coordinate = (screen_height // 2) - (window_size // 2)  # Calculate y-coordinate for centering the window

app_window.geometry(f"{window_size}x{window_size}+{x_coordinate}+{y_coordinate}")  # Set window size and position

app_window.iconbitmap("WeatherApplication/empty.ico")  # Set the application icon

bg_label = tk.Label(app_window)  # Create a label to hold the background image
bg_label.place(relwidth=1, relheight=1)  # Ensure the label covers the entire window
load_background_image("Weather-Application-main/images/default.jpg", app_window.winfo_width(), app_window.winfo_height())  # Load the default background image

title_label = tk.Label(app_window, text="PARV'S WEATHER APP", font=("Times New Roman", 28, "bold"))  # Title label configuration
title_label.place(relx=0.5, rely=0.35, anchor="center")  # Place title label at the center above the search bar

city_input = ttk.Entry(app_window, font=("Times New Roman", 18))  # Create an entry field for city input
city_input.insert(0, "Search City")  # Set default text for the entry field
city_input.bind("<FocusIn>", lambda e: city_input.delete(0, tk.END))  # Clear entry field when focused
city_input.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.08)  # Place input field at the center

search_button = ttk.Button(app_window, text="Get Weather", command=display_weather, bootstyle="primary")  # Create search button with action\search_button.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.35, relheight=0.075)  # Place search button below input field

weather_frame = tk.Frame(app_window, bg="#2b2b2b", bd=2, relief="solid")  # Create a frame to display weather details

location_display = tk.Label(weather_frame, font=("Times New Roman", 20))  # Label for displaying location
temp_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying temperature
feels_like_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying 'feels like' temperature
desc_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying weather description
humidity_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying humidity
wind_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying wind direction
pressure_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying atmospheric pressure
temp_min_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying minimum temperature
temp_max_display = tk.Label(weather_frame, font=("Times New Roman", 14))  # Label for displaying maximum temperature

for widget in [location_display, temp_display, feels_like_display, desc_display, 
               humidity_display, wind_display, pressure_display, temp_min_display, temp_max_display]:
    widget.pack_forget()  # Hide all weather detail labels initially

app_window.resizable(False, False)  # Disable window resizing
app_window.mainloop()  # Start the Tkinter event loop
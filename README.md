# Weather Application

This is a Python-based Weather Application that uses the OpenWeatherMap XML API to fetch and display real-time weather information for any city. The application is built using the `tkinter` library for the GUI and styled with `ttkbootstrap`.

## Features

- **Fetch Weather Details**: Retrieve weather data including temperature, humidity, wind direction, pressure, and weather conditions for a specified city.
- **Dynamic Background**: The background image changes based on the current weather condition.
- **Responsive UI**: Displays weather information in a user-friendly interface with an intuitive layout.
- **Error Handling**: Provides feedback when an invalid city name is entered.

## Requirements

To run this application, ensure the following dependencies are installed:

- Python 3.7+
- `tkinter` (comes pre-installed with Python)
- `ttkbootstrap`
- `Pillow`
- `requests`

You can install the required libraries using pip:

```bash
pip install ttkbootstrap pillow requests
```

## Setup and Installation

1. Clone the repository or download the source code:

```bash
git clone https://github.com/your-username/weather-application.git
cd weather-application
```

2. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/). Replace the `api_key` variable in the `weatherOf` function with your API key.

3. Ensure the following directory structure exists for the background images:

```
Weather-Application-main/
├── images/
│   ├── clearsky.png
│   ├── raining.png
│   ├── cloudy.jpg
│   ├── haze.png
│   └── mist.jpg
```

Replace these images with your own if needed.

4. Run the application:

```bash
python weather_app.py
```

## Usage

1. Launch the application.
2. Enter the name of a city in the input field.
3. Click the "Get Weather" button to fetch and display the weather information.
4. The background image will change based on the current weather condition.

## File Overview

- `weather_app.py`: Main application file containing the GUI and weather-fetching logic.
- `images/`: Directory containing background images for various weather conditions.

## Example

- **City Input**: Enter "New York" and press "Get Weather".
- **Output**: Displays weather details for New York, including temperature, humidity, and condition (e.g., "clear sky").

## Future Improvements

- Add support for more weather conditions and corresponding images.
- Display additional weather metrics like sunrise and sunset times.
- Provide a dropdown for recently searched cities.

## License

This project is licensed under the GNU General Public License v3.0.

## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/) for providing weather data.
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) for enhancing the tkinter interface.

## Contact

For any questions or suggestions, please contact [parvsinghal02@gmail.com].

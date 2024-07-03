# File to see the current weather forecast

# Import required modules
import ai_speak
import requests


def get_weather(api_key, city):
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant weather information
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Display weather information
        # print(f"Weather in {city}:")
        # print(f"Description: {description}")
        # print(f"Temperature: {temperature}°C")
        # print(f"Humidity: {humidity}%")
        # print(f"Wind Speed: {wind_speed} m/s")
        response = f"Weather in {city}: \nDescription: {description} \nTemperature: {temperature} \nHumidity: {humidity}% \nWind Speed: {wind_speed} m/s"
        # Speak weather information
        # ai_speak.speak(f"Weather in {city}:")
        # ai_speak.speak(f"Description: {description}")
        # ai_speak.speak(f"Temperature: {temperature}°C")
        # ai_speak.speak(f"Humidity: {humidity}%")
        # ai_speak.speak(f"Wind Speed: {wind_speed} m/s")
        return response
    else:
        # Display error message if request was not successful
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        ai_speak.speak(f"Error: Unable to fetch weather data. Status code: {response.status_code}")



import requests


API_KEY = 'fbb6b03821ea391d1d6574b4d8d464d9'


BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = 'Bopal'

url = f'{BASE_URL}q={city_name}&appid={API_KEY}'

response = requests.get(url)


data = response.json()


if data['cod'] == 200:
    # Extract and print weather information
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"Weather in {city_name}: {weather}")
    print(f"Temperature: {temp} k")
    print(f"Humidity: {humidity}%")
else:
    print("City not found!")
import requests

def weather_check():
    token = "f78ac47de8b6e1743864f8ff0e926814"
    city = input("Podaj miejscowość:")
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': token,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return "Nie udało się wykonać kodu"

weather_data = weather_check()
humidity = {weather_data['main']['humidity']}
temperature = {weather_data['main']['temp']}
wind_speed = {weather_data['wind']['speed']}
pressure = {weather_data['main']['pressure']}
degrees = {weather_data['wind']['deg']}

print(weather_data)

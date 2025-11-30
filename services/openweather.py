from config import Config
import requests
import json
import datetime

URL=f'https://api.openweathermap.org/data/2.5/weather?q={Config.QUERY}&appid={Config.API_KEY}'


def kelvintocelsius(kelv):
    celsius=kelv-273.15
    return round(celsius,2)

def fetchweather():
    try:
        response = requests.request("GET", URL)
        data=response.text #to co wychodzi z responsa w postaci stringa (to jest odkładnie tutaj napisane)
        jsondata=json.loads(data) #następuje konwersja ze stringa na dictionary
        tempcelsius=kelvintocelsius(jsondata['main']['temp'])
        feels_likecelsius=kelvintocelsius(jsondata['main']['feels_like'])
        result={
            "temp":tempcelsius,
            "feels_like":feels_likecelsius,
            "pressure":jsondata['main']['pressure'],
            "humidity":jsondata['main']["humidity"],
            "desciption":jsondata['weather'][0]['description'],
            "clouds":jsondata['clouds']['all'],
            "city":jsondata['name'],
            "wind speed":jsondata["wind"]['speed'],
            "wind direction in degree":jsondata["wind"]['deg'],
            "timestamp":datetime.datetime.now().strftime("%x %X")
        }
    except Exception as e:#wyłapuje mi błąd i go printuje go sobie fajnie, a trzymam go w tymczasowej zmiennej e
        print(e)
        print('Błąd URL!')
    else:
        print('Zalogowano się do API z OpenWeather i zostały pobrane dane!')
        return result


# temperatura, odczuwalna temp, ciśnienie, wilgotność, opis, zachmurzenie, miasto, wiatr, timestamp

import requests
import pprint


class RapidWeatherForecast:

    def get(self, city):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        query_param = {"units": "%22metric%22 or %22imperial%22", "mode": "xml%2C html", "q": city}
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "38a752497cmshebd70bc205d7128p1e3ed8jsn90527581d9a3"
        }
        print("SENDING HTTP REQUEST")
        data = requests.request('GET',url,headers=headers,params=query_param)
        data = data.json()
        # main,wind,clouds
        data_main,data_wind,data_clouds=data['main'],data['wind'],data['clouds']
        data_main['temp'] = data_main['temp'] - 273
        data_main['temp'] = round(data_main['temp'])
        data_final_main = {}
        data_final_main['Температура'] = data_main['temp']
        data_main['feels_like'] = data_main['feels_like'] - 273
        data_main['feels_like'] = round(data_main['feels_like'])
        data_final_main['Ощущается как'] = data_main['feels_like']
        data_main['temp_max'] = data_main['temp_max'] - 273
        data_main['temp_max'] = round(data_main['temp_max'])
        data_final_main['Максимальная температура'] = data_main['temp_max']
        data_main['temp_min'] = data_main['temp_min'] - 273
        data_main['temp_min'] = round(data_main['temp_min'])
        data_final_main['Минимальная температура'] = data_main['temp_min']
        return {'data':f'В городе {city} {data_final_main} градусов'}


class CityInfo:

    def __init__(self,city,weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or RapidWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

    def __str__(self):
        return self.city

city = CityInfo('Bishkek')
city_info = city.weather_forecast()
pprint.pprint(city_info)






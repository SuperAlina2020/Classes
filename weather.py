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
        return data_main,data_wind,data_clouds

class CityInfo:

    def __init__(self,city,weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or RapidWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

    def __str__(self):
        return self.city

city = CityInfo('Dubai')
city_info = city.weather_forecast()
pprint.pprint(city_info)





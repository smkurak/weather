from distutils.command.config import LANG_EXT
import requests
from django.shortcuts import render
from weather.forms import submitForm


def index(request):
  form = submitForm() # instantiate a new form here
  return render(request, 'weather/index.html', {'form': form}) # pass that form to the template


# def index(request):
#     appid = '8b0c5272341b36985647b10e8aba1492'
    
#     lat1 = 55.840814
#     lon1 = 37.744220
    
#     url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid='.format(lat1,lon1)+appid


#     res = requests.get(url).json()
    
#     city_info = {
#         'name':res["name"],
#         'lat1':res["coord"]["lat"],
#         'temp':res["main"]["temp"], 
#         'icon':res["weather"][0]["icon"]
#     }

#     contex = {'info': city_info}
    


#     return render(request, 'weather/index.html', contex)


    # {"coord":{"lon":37.7442,"lat":55.8408},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"base":"stations","main":{"temp":287.21,"feels_like":287.15,"temp_min":286.66,"temp_max":288.14,"pressure":1007,"humidity":95,"sea_level":1007,"grnd_level":986},"visibility":5425,"wind":{"speed":3.43,"deg":184,"gust":9.45},"rain":{"1h":1.04},"clouds":{"all":100},"dt":1664651818,"sys":{"type":2,"id":47754,"country":"RU","sunrise":1664595073,"sunset":1664636771},"timezone":10800,"id":6418787,"name":"Metrogorodok","cod":200}
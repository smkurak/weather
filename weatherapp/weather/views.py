import requests
from django.shortcuts import render

def index(request):
    appid = '8b0c5272341b36985647b10e8aba1492'
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid
    city = 'London'
    res = requests.get(url.format(city)).json()
    
    city_info = {
        'city':city,
        'temp':res["main"]["temp"], 
        'icon':res["weather"][0]["icon"]
    }

    contex = {'info': city_info}
    


    return render(request, 'weather/index.html', contex)
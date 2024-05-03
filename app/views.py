from django.shortcuts import render

import os 
import requests

API_KEY = os.environ['weather_api']
BASE_URL = 'http://api.weatherapi.com/v1/current.json?key='
print(API_KEY)

# Create your views here.
def home(request):
    
    city_from_request = request.GET.get('search-bar') or 'London'
    print(city_from_request)
    
    response = requests.get(f'{BASE_URL}{API_KEY}&q={city_from_request}')
    json_response = response.json()
    print(json_response)
    city = json_response['location']['name']
    temp_c = json_response['current']['temp_c']
    condition = json_response['current']['condition']['text']
    img = json_response['current']['condition']['icon']
    wind = json_response['current']['wind_kph']
    local_time = json_response['location']['localtime']
    humidity = json_response['current']['humidity']
    
    
    return render(request, 'accounts/home.html', {
        'city': city,
        'temp_c': temp_c,
        'condition': condition,
        'icon': img,
        "wind": wind,
        'local_time': local_time,
        'humidity': humidity
    })

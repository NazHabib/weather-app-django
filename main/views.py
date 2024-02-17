

import urllib.request
import json
from django.shortcuts import render

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city')  # Use .get for safer dictionary access

        # Your API key - replace 'your_api_key_here' with your actual OpenWeatherMap API key
        appid = "Your_code"

        try:
            # Construct the API URL with the city and your API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}"
            source = urllib.request.urlopen(url).read()

            # Converting JSON data to a dictionary
            list_of_data = json.loads(source)

            # Data for variable list_of_data
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temp": f"{list_of_data['main']['temp']}k",
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except Exception as e:
            print(f"Error: {e}")
            data = {
                "error": "Could not retrieve data from OpenWeatherMap API. Please check your city name and API key."
            }

    return render(request, "main/index.html", data)

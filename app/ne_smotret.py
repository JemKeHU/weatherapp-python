import requests
import json
from geopy.geocoders import Nominatim

def get_location(name):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(name)
    return getLoc.latitude, getLoc.longitude

url = "https://api.open-meteo.com/v1/forecast"

lat, longt = get_location(input())

params = {
	"latitude": lat,
	"longitude": longt,
	"hourly": "temperature_2m",
	"timezone": "Europe/Moscow",
	"past_days": 3,
	"forecast_days": 3
}

response_API = requests.get(url=url, params=params)
data = response_API.text
parse_json = json.loads(data)
print(json.dumps(parse_json, indent=4))
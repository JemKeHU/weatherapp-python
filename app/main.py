from fastapi import FastAPI
import requests
import json
from geopy.geocoders import Nominatim
from fastapi.responses import FileResponse

def get_location(name):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(name)
    if getLoc:
        return getLoc.latitude, getLoc.longitude
    else:
        return None, None

app = FastAPI()

@app.get("/weather city={city_name}")
def root(city_name: str):
    url = "https://api.open-meteo.com/v1/forecast"

    lat, longt = get_location(city_name)

    if not lat and not longt:
        return FileResponse("404.html")

    params = {
        "latitude": lat,
        "longitude": longt,
        "daily": ",".join(["temperature_2m_max", "temperature_2m_mean", "temperature_2m_min", "weathercode", "cloudcover_mean", "pressure_msl_max", "pressure_msl_min"]),
        "timezone": "Europe/Moscow",
    }

    response_API = requests.get(url=url, params=params)
    data = response_API.json()

    try:
        today = {
            "date": data["daily"]["time"][0],
            "city_name": city_name,
            "temp_max": data["daily"]["temperature_2m_max"][0],
            "temp_mean": data["daily"]["temperature_2m_mean"][0],
            "temp_min": data["daily"]["temperature_2m_min"][0],
            "pressure_max": data["daily"]["pressure_msl_max"][0],
            "pressure_min": data["daily"]["pressure_msl_min"][0], 
            "clouds": data["daily"]["cloudcover_mean"][0],
            "weather_code": data["daily"]["weathercode"][0]
            # создатели документации дети шлюх пидорасы гниды, в доке пишут одно, а записывать друг
        }
    except KeyError as e:
        return {"error": f"Missing key in API response: {e}"}

    return today
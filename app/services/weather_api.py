from schemas.weather_by_response import WeatherByCityResponse
from config import weather_api_url
from requests import get

class WeatherAPI:
    def weather_for_city(self, city: str, lat: float, longt: float) -> WeatherByCityResponse:
        params = {
            "latitude": lat,
            "longitude": longt,
            "daily": ",".join(["temperature_2m_max", "temperature_2m_mean", "temperature_2m_min", "weathercode", "cloudcover_mean", "pressure_msl_max", "pressure_msl_min"]),
            "timezone": "Europe/Moscow",
        }

        response_API = get(url=weather_api_url, params=params)
        data = response_API.json()

        try:
            today = {
                "date": data["daily"]["time"][0],
                "city_name": city,
                "temp_max": data["daily"]["temperature_2m_max"][0],
                "temp_mean": data["daily"]["temperature_2m_mean"][0],
                "temp_min": data["daily"]["temperature_2m_min"][0],
                "pressure_max": data["daily"]["pressure_msl_max"][0],
                "pressure_min": data["daily"]["pressure_msl_min"][0], 
                "clouds": data["daily"]["cloudcover_mean"][0],
                "weather_code": data["daily"]["weathercode"][0]
            }

            return today
        except KeyError as e:
            return {"error": f"Missing key in API response: {e}"}
        
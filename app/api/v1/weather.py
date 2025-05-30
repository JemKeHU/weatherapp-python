from fastapi import APIRouter, HTTPException
from schemas.weather_by_response import WeatherByCityResponse
from schemas.weather_for_city_request import WeatherForCityRequest
from services.nominatim import get_location
from services.weather_api import WeatherAPI

router = APIRouter(prefix="/weather", tags=["Weather"])

@router.post("/", response_model=WeatherByCityResponse)
def get_weather_for_city(city_data: WeatherForCityRequest):
    lat, longt = get_location(city_data)

    if not lat and not longt:
        raise HTTPException(status_code=404, detail="City is not found")
    
    weather_api = WeatherAPI()

    return weather_api.weather_for_city(city_data.city, lat, longt)
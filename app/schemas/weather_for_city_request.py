from pydantic import BaseModel

class WeatherForCityRequest(BaseModel):
    city: str
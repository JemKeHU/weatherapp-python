from datetime import datetime
from pydantic import BaseModel

class WeatherByCityResponse(BaseModel):
    date: datetime
    city_name: str
    temp_max: float
    temp_mean: float
    temp_min: float
    pressure_max: float
    pressure_min: float
    clouds: int
    weather_code: int
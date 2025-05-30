from fastapi import FastAPI
from api.v1.weather import router as weather_router

app = FastAPI()

app.include_router(router=weather_router, prefix="/api/v1")
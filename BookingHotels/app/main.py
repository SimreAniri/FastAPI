from datetime import date
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

class HotelsSearchArgs:
    def __init__(self,
                 location: str,
                 date_from: date,
                 date_to: date,
                 stars: int = Query(default=None, ge=1, le=5),
                 get_spa: bool = Query(default=None),) -> None:
        self.location = location,
        self.date_from = date_from,
        self.date_to = date_to,
        self.stars = stars,
        self.get_spa = get_spa

class SHotel(BaseModel):
    address: str
    name: str
    stars: int = Field(ge=1, le=5)

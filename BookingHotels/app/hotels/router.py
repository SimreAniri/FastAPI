from datetime import date
from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotels


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

@router.get("")
async def get_hotels(
    location: str,
    date_from: date, 
    date_to: date,
):
    return await HotelsDAO.find_all(location, date_from, date_to)
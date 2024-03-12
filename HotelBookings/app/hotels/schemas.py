from pydantic import BaseModel

class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

class SLeftRoomsInHotels(SHotels):
    count_left_rooms: int
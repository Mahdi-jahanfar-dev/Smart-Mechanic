from pydantic import BaseModel
from core.enum import CarRepairRatingEnum


# schema for register car
class CarRegisterSchema(BaseModel):

    brand: str
    model: str


# schema for accept car repair
class AcceptCarRepairSchema(BaseModel):

    repaired: bool
    rating: CarRepairRatingEnum

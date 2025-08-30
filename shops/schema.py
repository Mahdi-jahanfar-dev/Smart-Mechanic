from pydantic import BaseModel
from accounts.schema import UserSchema
from datetime import datetime


# schema for showing the list of mechanics
class MechanicShopsListSchema(BaseModel):
    name: str
    owner: UserSchema
    address: str


# schema for creating mechanic shop
class MechanicCreateSchema(BaseModel):
    name: str
    description: str
    address: str


# schema for showing mechanic shop details
class MechanicDetailSchema(BaseModel):
    name: str
    description: str
    address: str
    owner: UserSchema


# schema for register mechanic reservation
class MechanicResevationCreateSchema(BaseModel):

    date: datetime
    car_id: int
    shop_id: int

from pydantic import BaseModel
from accounts.schema import UserSchema
from datetime import datetime


class MechanicShopsListSchema(BaseModel):
    name: str
    owner: UserSchema
    address: str


class MechanicCreateSchema(BaseModel):
    name: str
    description: str
    address: str


class MechanicDetailSchema(BaseModel):
    name: str
    description: str
    address: str
    owner: UserSchema


class MechanicResevationCreateSchema(BaseModel):

    date: datetime
    car_id: int
    shop_id: int

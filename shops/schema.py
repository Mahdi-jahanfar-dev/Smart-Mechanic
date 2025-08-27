from pydantic import BaseModel
from accounts.schema import UserSchema


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

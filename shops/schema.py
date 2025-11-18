from pydantic import BaseModel
from accounts.schema import UserSchema
from datetime import datetime
from core.enum import CreateReservationStatusEnum


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


# this schema using enum for choose status
class MechanicChooseStatusSchema(BaseModel):
    status: CreateReservationStatusEnum


class MechanicLaborCostSchema(BaseModel):
    rust = int
    scratches = int
    dents = int
    bad_odor = int
    strange_noises = int
    no_cooling = int
    malfunctioning_lights = int
    faulty_starter = int
    dead_battery = int
    uneven_tire_wear = int
    wobbling = int
    misalignment = int
    vibration_when_braking = int
    reduced_responsiveness = int
    squeaking_noises = int
    grinding_noises = int
    clutch_slip = int
    difficulty_shifting = int
    delayed_acceleration = int
    transmission_fluid_leak = int
    harsh_shifting = int
    strange_noises = int
    oil_leak = int
    overheating = int
    low_engine_oil = int
    weak_battery = int
    flat_tire = int
    low_brake_oil = int
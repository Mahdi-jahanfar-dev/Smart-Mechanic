from pydantic import BaseModel


# schema for register car
class CarRegisterSchema(BaseModel):

    brand: str
    model: str

from pydantic import BaseModel


class CarRegisterSchema(BaseModel):

    brand: str
    model: str

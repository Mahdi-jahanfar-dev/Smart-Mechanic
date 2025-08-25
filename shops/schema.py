from pydantic import BaseModel


class MechanicShopsList(BaseModel):
    name: str
    owner: str
    address: str
from core.database_config import Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class MechanicShop(Base):

    __tablename__ = "shops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    address = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    owner = relationship("User", back_populates="mechanic_shop")

    def __repr__(self):
        return f"{self.name}-{self.owner.username}"
    
    
class MechanicReservation(Base):
    
    __tablename__ = "resevations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    shop_id = Column(Integer, ForeignKey("shops.id"))
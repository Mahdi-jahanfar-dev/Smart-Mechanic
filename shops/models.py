from core.database_config import Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship


# mechanic shop model
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


# mechanic shop reservation model
class MechanicReservation(Base):

    __tablename__ = "resevations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    shop_id = Column(Integer, ForeignKey("shops.id"))
    status = Column(String)
    rating = Column(Integer)
    description = Column(Text)


# the price for each service
class MechanicLaborCost(Base):
    __tablename__ = "costs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rust = Column(Integer, default=0, nullable=False)
    scratches = Column(Integer, default=0, nullable=False)
    dents = Column(Integer, default=0, nullable=False)
    bad_odor = Column(Integer, default=0, nullable=False)
    strange_noises = Column(Integer, default=0, nullable=False)
    no_cooling = Column(Integer, default=0, nullable=False)
    malfunctioning_lights = Column(Integer, default=0, nullable=False)
    faulty_starter = Column(Integer, default=0, nullable=False)
    dead_battery = Column(Integer, default=0, nullable=False)
    uneven_tire_wear = Column(Integer, default=0, nullable=False)
    wobbling = Column(Integer, default=0, nullable=False)
    misalignment = Column(Integer, default=0, nullable=False)
    vibration_when_braking = Column(Integer, default=0, nullable=False)
    reduced_responsiveness = Column(Integer, default=0, nullable=False)
    squeaking_noises = Column(Integer, default=0, nullable=False)
    grinding_noises = Column(Integer, default=0, nullable=False)
    clutch_slip = Column(Integer, default=0, nullable=False)
    difficulty_shifting = Column(Integer, default=0, nullable=False)
    delayed_acceleration = Column(Integer, default=0, nullable=False)
    transmission_fluid_leak = Column(Integer, default=0, nullable=False)
    harsh_shifting = Column(Integer, default=0, nullable=False)
    strange_noises = Column(Integer, default=0, nullable=False)
    oil_leak = Column(Integer, default=0, nullable=False)
    overheating = Column(Integer, default=0, nullable=False)
    low_engine_oil = Column(Integer, default=0, nullable=False)
    weak_battery = Column(Integer, default=0, nullable=False)
    flat_tire = Column(Integer, default=0, nullable=False)
    low_brake_oil = Column(Integer, default=0, nullable=False)

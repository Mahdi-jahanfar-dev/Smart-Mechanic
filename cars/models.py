from core.database_config import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref


# user car model
class Car(Base):

    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    model = Column(String)
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
        ),
    )

    owner = relationship("User", back_populates="cars")

    def __repr__(self):
        return f"{self.owner.username}-{self.brand}-{self.model}"


class MainProblemModel(Base):
    __tablename__ = "main_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    car_id = Column(
        Integer,
        ForeignKey(
            "cars.id",
        ),
    )

    car = relationship(
        "Car", backref=backref("main_problems", cascade="all, delete-orphan")
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"
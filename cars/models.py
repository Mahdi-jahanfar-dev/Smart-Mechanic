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


# basic problem model (for problems like low engine oil, weak battery, etc.)
class BasicProblemModel(Base):
    __tablename__ = "basic_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    low_engine_oil = Column(Boolean, default=False)
    weak_battery = Column(Boolean, default=False)
    flat_tire = Column(Boolean, default=False)
    low_brake_oil = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("basic_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# main problem model (this model will have relationship with all other problem models)
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

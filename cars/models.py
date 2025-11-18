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


# motor problem model (for problems like overheating, oil leak, etc.)
class MotorProblemModel(Base):
    __tablename__ = "motor_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    overheating = Column(Boolean, default=False)
    oil_leak = Column(Boolean, default=False)
    strange_noises = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("motor_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# transmission automatic problem model (for problems like harsh shifting, fluid leak, etc.)
class TransmissionAutomaticProblemModel(Base):
    __tablename__ = "transmission_automatic_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    harsh_shifting = Column(Boolean, default=False)
    transmission_fluid_leak = Column(Boolean, default=False)
    delayed_acceleration = Column(Boolean, default=False)

    main_transmission_problem = Column(
        Integer,
        ForeignKey(
            "main_transmission_problems.id",
        ),
    )

    main_transmission_prob = relationship(
        "MainProblemModel",
        backref=backref(
            "transmission_automatic_problems", cascade="all, delete-orphan"
        ),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# transmission manual problem model (for problems like difficulty shifting, clutch slip, etc.)
class TransmissionManualProblemModel(Base):
    __tablename__ = "transmission_manual_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    difficulty_shifting = Column(Boolean, default=False)
    clutch_slip = Column(Boolean, default=False)
    grinding_noises = Column(Boolean, default=False)

    main_transmission_problem = Column(
        Integer,
        ForeignKey(
            "main_transmission_problems.id",
        ),
    )

    main_transmission_prob = relationship(
        "MainProblemModel",
        backref=backref("transmission_manual_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# transmission main problem model (this model will have relationship with both automatic and manual transmission problem models)
class TransmissionMainProblemModel(Base):
    __tablename__ = "main_transmission_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("transmission_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# brake problem model (for problems like squeaking noises, reduced responsiveness, etc.)
class BrakeProblemModel(Base):
    __tablename__ = "brake_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    squeaking_noises = Column(Boolean, default=False)
    reduced_responsiveness = Column(Boolean, default=False)
    vibration_when_braking = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("brake_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# wheel problem model (for problems like misalignment, wobbling, etc.)
class WheelProblemModel(Base):
    __tablename__ = "wheel_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    misalignment = Column(Boolean, default=False)
    wobbling = Column(Boolean, default=False)
    uneven_tire_wear = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("wheel_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# electrical problem model (for problems like dead battery, faulty starter, etc.)
class ElectricalProblemModel(Base):
    __tablename__ = "electrical_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    dead_battery = Column(Boolean, default=False)
    faulty_starter = Column(Boolean, default=False)
    malfunctioning_lights = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("electrical_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# havac problem model (for problems like no cooling, strange noises, etc.)
class HavacProblemModel(Base):
    __tablename__ = "havac_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    no_cooling = Column(Boolean, default=False)
    strange_noises = Column(Boolean, default=False)
    bad_odor = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("havac_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


class BodyProblemModel(Base):
    __tablename__ = "body_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    dents = Column(Boolean, default=False)
    scratches = Column(Boolean, default=False)
    rust = Column(Boolean, default=False)

    main_problem_id = Column(
        Integer,
        ForeignKey(
            "main_problems.id",
        ),
    )

    main_prob = relationship(
        "MainProblemModel",
        backref=backref("body_problems", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        return f"{self.car.brand}-{self.car.model}-{self.description}"


# main problem model (this model will have relationship with all other problem models)
class MainProblemModel(Base):
    __tablename__ = "main_problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
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

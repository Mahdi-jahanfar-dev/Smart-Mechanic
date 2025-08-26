from core.database_config import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


class Car(Base):

    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    model = Column(String)
    user_id = Column(
        ForeignKey(
            "users.id",
        )
    )

    owner = relationship("User", back_populates="cars")

    def __repr__(self):
        return f"{self.owner.username}-{self.brand}-{self.model}"

from core.database_config import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from passlib.context import CryptContext
from sqlalchemy.orm import relationship


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(length=100))
    first_name = Column(String(length=100))
    last_name = Column(String(length=100))
    is_mechanic = Column(Boolean, default=False)
    password = Column(String(length=200))
    registred_at = Column(
        DateTime,
    )
    is_admin = Column(Boolean, default=False)
    
    cars = relationship("Car", back_populates="owner")

    def validate(self, entry_password):
        return pwd_context.verify(entry_password, self.password)

    def __repr__(self):
        return self.username

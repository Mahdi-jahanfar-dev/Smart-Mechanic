from core.database_config import session, Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password: str) -> str:
    pwd_context.hash(password)

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(length=100))
    first_name = Column(String(length=100))
    last_name = Column(String(length=100))
    is_mechanic = Column(Boolean, default=False)
    password = Column(String(length=200))
    registred_at = Column(DateTime,)
    
    def validate(self, entry_password):
        pwd_context.verify(entry_password, self.password)
        
    def __repr__(self):
        return self.username
    
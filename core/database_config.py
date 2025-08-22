from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
from sqlalchemy.orm import declarative_base


engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

session = SessionLocal()

Base = declarative_base()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()

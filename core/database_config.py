from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
from sqlalchemy.orm import declarative_base

DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORTS}/{settings.POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

session = SessionLocal()

Base = declarative_base()


# db instance
def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from .config import settings
from accounts.models import User
from .database_config import Base, engine


app = FastAPI()


Base.metadata.create_all(engine)

@app.get("/")
def test():
    return {"message": f"hi user this is test route"}
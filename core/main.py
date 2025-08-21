from fastapi import FastAPI
from .config import settings


app = FastAPI()


@app.get("/")
def test():
    return {"message": f"hi user this is test route"}
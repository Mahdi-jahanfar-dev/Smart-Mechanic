from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def test():
    return {"message": "hi user this is test route"}
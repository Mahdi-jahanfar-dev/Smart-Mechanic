from fastapi import FastAPI
from .config import settings
from accounts.models import User
from .database_config import Base, engine
from accounts.routes import router as accounts_router


app = FastAPI()


Base.metadata.create_all(engine)


@app.get("/")
def test():
    return {"message": f"hi user this is test route"}


# account app routes
app.include_router(accounts_router)

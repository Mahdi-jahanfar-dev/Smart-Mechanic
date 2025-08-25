from fastapi import FastAPI
from accounts.routes import router as accounts_router
from shops.routes import router as shops_router


app = FastAPI()


@app.get("/")
def test():
    return {"message": f"hi user this is test route"}


# account app routes
app.include_router(accounts_router)
app.include_router(shops_router)

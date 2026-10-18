from fastapi import FastAPI
from app.routers import users


app = FastAPI(title="My API",version="1.0.0")

app.include_router(users.router)

'''@app.get("/")
def read_root():
    return {"message": "Hello, world"}'''
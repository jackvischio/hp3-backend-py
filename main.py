from fastapi import FastAPI
from routes.campionati import route

app = FastAPI()

app.include_router(route)

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}

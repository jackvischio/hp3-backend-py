from fastapi import FastAPI
from routes.campionati import route as routeCamp
from routes.arbitri import route as routeRef

app = FastAPI()

app.include_router(routeCamp)
app.include_router(routeRef)

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}

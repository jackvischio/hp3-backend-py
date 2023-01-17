from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.campionati import route as routeCamp
from routes.arbitri import route as routeRef
from routes.partite import route as routePart
from routes.squadre import route as routeSquad

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routeCamp)
app.include_router(routeRef)
app.include_router(routePart)
app.include_router(routeSquad)

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}

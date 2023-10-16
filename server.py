from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.competizioni import route as routeCompetizioni
from routes.calendario import route as routeCalendario

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routeCompetizioni)
app.include_router(routeCalendario)

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}

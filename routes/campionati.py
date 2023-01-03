from fastapi import APIRouter, HTTPException

from models.campionato import Campionato
from database import connection
from serializers import serializeItem, serializeList

route = APIRouter()

@route.get('/campionati/', response_model=list[Campionato])
async def find_all_camps():
    return serializeList(connection.hockeypista.campionati.find())

@route.get('/campionati/stagione/{idStagione}', response_model=list[Campionato])
async def find_all_camps(idStagione: int):
    if id:
        camps = connection.hockeypista.campionati.find({"stagione": int(idStagione)})
        if camps and len(list(camps.clone())) > 0:
            return serializeList(camps)
        raise HTTPException(404, "Nessun campionato associato alla stagione")
    raise HTTPException(403, "Parametro id stagione mancante")

@route.get('/campionato/{id}', response_model=Campionato)
async def find_camp(id: int):
    if id:
        camp = connection.hockeypista.campionati.find_one({"id": int(id)})
        if camp:
            return serializeItem(camp)
        raise HTTPException(404, "Campionato non trovato")
    raise HTTPException(403, "Parametro id mancante")
from fastapi import APIRouter, HTTPException

from database import connection
from serializers import serializeItem

route = APIRouter()

@route.get('/squadra/{id}')
async def get_squadra(id: int):
    if id:
        partita = connection.hockeypista.squadre.find_one({"id": int(id)})
        if partita:
            return serializeItem(partita)
        raise HTTPException(404, "Squadra non trovata")
    raise HTTPException(403, "Parametro id squadra mancante")
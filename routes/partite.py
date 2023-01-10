from fastapi import APIRouter, HTTPException

from database import connection
from serializers import serializeItem

route = APIRouter()

@route.get('/partita/{id}')
async def find_all_camps(id: int):
    if id:
        partita = connection.hockeypista.partite.find_one({"id": int(id)})
        if partita:
            return serializeItem(partita)
        raise HTTPException(404, "Partita non trovata")
    raise HTTPException(403, "Parametro id partita mancante")
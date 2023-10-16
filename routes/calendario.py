from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union
import time
from mysqldb import connection
import datetime

# Modello per la risposta dell'API
class Calendario(BaseModel):
    compId: int
    faseId: int
    faseRuolo: str
    faseNome: str
    giornId: int
    giornRuolo: str
    giornNome: str
    idp: Union[int, None]
    data: str
    ora: str
    squadra1: int
    squadra2: int
    risultato: Union[str, None]

    class Config:
        orm_mode = True

# API effettiva
route = APIRouter()

@route.get("/calendario/{competizione}", response_model=list[Calendario])
def read_item(competizione):
    start_time = time.time()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM calendario_view WHERE compId=%s"
    cursor.execute(query, (competizione,))
    items = cursor.fetchall()
    cursor.close()
    for item in items:
        item['data'] = datetime.strftime(item['data'])
    print("Execution time: {} sec".format(time.time() - start_time))
    if items is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return items
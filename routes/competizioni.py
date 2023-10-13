from fastapi import APIRouter, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalc import Base
from pydantic import BaseModel
from sqlalc import SessionLocal
from typing import Union
import time
from mysqldb import connection

# Entity per il DB
class Entity(Base):
    __tablename__ = "competizioni"

    id = Column("PK_competizione", Integer, primary_key=True, index=True)
    stagione = Column("FK_stagione", Integer)
    categoria = Column("E_categoria", String)
    nome = Column(String)
    tipo = Column(Integer)
    ordine = Column(Integer)

# Modello di risposta dell'API
class Competizione(BaseModel):
    id: int
    stagione: Union[int, None] = None
    categoria: Union[str, None] = None
    nome: Union[str, None] = None
    tipo: Union[int, None] = None
    ordine: Union[int, None] = None

    class Config:
        orm_mode = True

# API effettiva
route = APIRouter()

db = SessionLocal()

@route.get("/competizioni/{stagione}/{categoria}", response_model=list[Competizione])
def competizioni_by_categoria(stagione: int, categoria: str):
    try:
        start_time = time.time()
        response = db.query(Entity).filter(Entity.stagione == stagione, Entity.categoria == categoria).all()
        print("Execution time: {} sec".format(time.time() - start_time))
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error on API execution")
    
@route.get("/competizioni/{stagione}", response_model=list[Competizione])
def competizioni_by_stagione(stagione: int):
    try:
        start_time = time.time()
        response = db.query(Entity).filter(Entity.stagione == stagione).all()
        print("Execution time: {} sec".format(time.time() - start_time))
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error on API execution")

@route.get("/competizioni_plain/{stagione}", response_model=list[Competizione])
def read_item(stagione):
    start_time = time.time()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT PK_competizione as id, E_categoria as categoria, FK_stagione as stagione, nome, tipo, ordine FROM competizioni WHERE FK_stagione=%s"
    cursor.execute(query, (stagione,))
    items = cursor.fetchall()
    cursor.close()
    print("Execution time: {} sec".format(time.time() - start_time))
    if items is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return items

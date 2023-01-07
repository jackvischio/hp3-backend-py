from fastapi import APIRouter

from models.arbitri import Coppia
from database import connection
from serializers import serializeList

route = APIRouter()

@route.get('/arbitri/stats/singoli/')
async def all_ref_stats():
    res1 = connection.hockeypista.designazioni.aggregate([
        {"$group" : {"_id":"$arbitro1", "partite":{ "$sum": 1}}},
        { "$sort": { "partite": -1 } }
    ])
    lista1 = { e['_id']: e['partite'] for e in list(res1)}
    res2 = connection.hockeypista.designazioni.aggregate([
        {"$group" : {"_id":"$arbitro2", "partite":{ "$sum": 1}}},
        { "$sort": { "partite": -1 } }
    ])
    lista2 = { e['_id']: e['partite'] for e in list(res2) if e['_id'] != None}

    for nome in lista2.keys():
        if nome in lista1.keys():
            lista1[nome] = lista1[nome] + lista2[nome]
        else:
            lista1['nome'] = lista2[nome]
    
    ret = [ {"nome": k, "partite": lista1[k] } for k in lista1.keys()]
    return sorted(ret, key=lambda e: int(e['partite']), reverse=True)

@route.get('/arbitri/stats/coppie/', response_model=list[Coppia])
async def all_ref_cop_stats():
    res = connection.hockeypista.designazioni.aggregate([
        { "$match": { "arbitro2": { "$exists": True, "$ne": None } } },
        { "$group" : {"_id": {"arbitro1" : "$arbitro1", "arbitro2" : "$arbitro2"}, "partite":{ "$sum": 1}}},
        { "$sort": { "partite": -1 } }
    ])
    lista = [{"arbitro1": e['_id']['arbitro1'], "arbitro2": e['_id']['arbitro2'], "partite": e['partite']} for e in res]
    return lista

@route.get('/arbitri/partite/{nome}/')
async def ref_stats(nome: str):
    aus = serializeList(connection.hockeypista.designazioni.find({'ausiliario': nome.upper()}))
    a1 = serializeList(connection.hockeypista.designazioni.find({'arbitro1': nome.upper()}))
    a2 = serializeList(connection.hockeypista.designazioni.find({'arbitro2': nome.upper()}))
    return { "nome": nome, "arbitro1": a1, "arbitro2": a2, "ausiliario": aus }
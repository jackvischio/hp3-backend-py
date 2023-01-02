from pydantic import BaseModel

class Campionato(BaseModel):
    id: int
    nome: str
    label: str
    logo: str
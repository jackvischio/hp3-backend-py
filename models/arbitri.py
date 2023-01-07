from pydantic import BaseModel

class Coppia(BaseModel):
    arbitro1: str
    arbitro2: str
    partite: int
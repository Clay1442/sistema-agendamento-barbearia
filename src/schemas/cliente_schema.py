from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    telefone: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id:int

    model_config = {"from_attributes": True}

class ClienteUpdate(ClienteBase):
   nome: Optional[str] = None
   telefone: Optional[str] = None
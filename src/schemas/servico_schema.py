from pydantic import BaseModel
from typing import Optional

# 1. Base: O que é comum para criar, ler e atualizar
class ServicoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    duracao_minutos: int

# 2. Create: O que o usuário envia no POST para criar um serviço
# (Como herda do Base, ele já tem nome, preço, etc.)
class ServicoCreate(ServicoBase):
    pass

# 3. Response: O que a sua API devolve para a internet no GET
class ServicoResponse(ServicoBase):
    id: int

    # Essa configuração é mágica: ensina o Pydantic a ler objetos do SQLAlchemy
    model_config = {"from_attributes": True}

# 4. Update: O que o usuário envia no PUT (tudo é opcional)
class ServicoUpdate(ServicoBase):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    duracao_minutos: Optional[int] = None
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.repositories.servico_repository import ServicoRepository

# Cria o roteador para esta entidade
router = APIRouter()

# Instancia o repositório que criamos no passo anterior
repo = ServicoRepository()

@router.get("/", response_model=List[ServicoResponse])
async def listar_servicos(db: AsyncSession = Depends(get_db)):
    """
    Retorna a lista de todos os serviços disponíveis na barbearia.
    """
    # Chama o repositório para buscar no banco
    servicos = await repo.get_all(db)
    
    # O FastAPI pega essa lista de objetos do banco e, magicamente, 
    # converte para JSON usando o `ServicoResponse` que definimos no response_model!
    return servicos

@router.get("/{servico_id}", response_model=ServicoResponse)
async def listar_servico_por_id(servico_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retorna os detalhes de um serviço específico, identificado pelo seu ID.
    """
    servico = await repo.get_by_id(db, servico_id)
    
    if not servico:
        return {"error": "Serviço não encontrado"}
    
    return servico
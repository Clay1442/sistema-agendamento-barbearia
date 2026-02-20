from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.repositories.servico_repository import ServicoRepository
from src.services.listar_servicos_use_case import ListarServicosUseCase

router = APIRouter()

@router.get(
    "/",
    tags=["Serviços"], 
    summary="Obter lista de serviços da babearia",
    response_model=List[ServicoResponse]
)
async def listar_todos_servicos(db: AsyncSession = Depends(get_db)):
    # Retorna a lista de todos os serviços disponíveis na barbearia.

    servicoRepository = ServicoRepository(db)

    listarServicosUseCase = ListarServicosUseCase(servicoRepository)

    servicos = await listarServicosUseCase.execute()
    
    return servicos

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.database import get_db
from src.schemas.cliente_schema import ClienteResponse
from src.repositories.cliente_repository import ClienteRepository
from src.use_case.client.listar_clientes_use_case import ListarClientesUseCase

router = APIRouter()

@router.get(
    "/",
    tags=["Clientes"], 
    summary="Obter lista de todos os clientes",
    response_model=List[ClienteResponse]
)
async def listar_todos_clientes(db: AsyncSession = Depends(get_db)):
    clienteRepository = ClienteRepository(db)
    listarClientesUseCase = ListarClientesUseCase(clienteRepository)
    clientes = await listarClientesUseCase.execute()
    return clientes
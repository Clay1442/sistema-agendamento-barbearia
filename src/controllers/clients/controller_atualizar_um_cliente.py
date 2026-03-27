from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.cliente_schema import ClienteResponse, ClienteUpdate
from src.repositories.cliente_repository import ClienteRepository
from src.use_case.client.atualizar_cliente_use_case import AtualizarClienteUseCase

router = APIRouter()

@router.put(
    "/{id}",
    tags=["Clientes"],
    summary="Atualizar informações de um cliente",
    response_model=ClienteResponse
)
async def atualizar_um_cliente(id: int, cliente_data: ClienteUpdate, db: AsyncSession = Depends(get_db)):
    clienteRepository = ClienteRepository(db)
    atualizarClienteUseCase = AtualizarClienteUseCase(clienteRepository)
    cliente = await atualizarClienteUseCase.execute(id, cliente_data)
    return cliente
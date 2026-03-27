from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.repositories.cliente_repository import ClienteRepository
from src.use_case.client.deletar_cliente_use_case import DeletarClienteUseCase

router = APIRouter()

@router.delete(
    "/{cliente_id}",
    tags=["Clientes"],
    summary="Excluir um cliente do sistema",
    status_code=status.HTTP_204_NO_CONTENT
)
async def deletar_um_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    # Deletar um cliente específico, identificado pelo seu ID.

    cliente_repository = ClienteRepository(db)
    deletarClienteUseCase = DeletarClienteUseCase(cliente_repository)

    await deletarClienteUseCase.execute(cliente_id)

    return None
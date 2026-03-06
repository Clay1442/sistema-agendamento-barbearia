from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.cliente_schema import ClienteResponse
from src.repositories.cliente_repository import ClienteRepository
from src.use_case.client.pegar_cliente_use_case import PegarClienteUseCase

router = APIRouter()

@router.get(
    "/{cliente_id}", 
    tags=["Clientes"],
    summary="Pegar um cliente pelo ID",
    response_model=ClienteResponse,
    )
async def pegar_um_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    # Pegar cliente pelo seu id
    cliente_repository = ClienteRepository(db)
    pegarClienteUseCase = PegarClienteUseCase(cliente_repository)

    cliente = await pegarClienteUseCase.execute(cliente_id)
    return cliente
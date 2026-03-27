from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.cliente_schema import ClienteCreate, ClienteResponse
from src.repositories.cliente_repository import ClienteRepository
from src.use_case.client.criar_cliente_use_case import CriarClienteUseCase

router = APIRouter()

@router.post(
    "/",
    tags=["Clientes"],
    summary="Cadastrar um novo cliente",
    response_model=ClienteResponse,
    status_code=status.HTTP_201_CREATED
)

async def cadastrar_um_cliente(cliente_data: ClienteCreate, db: AsyncSession = Depends(get_db)):
    # Cadastrar um novo cliente no sistema.

    cliente_repository = ClienteRepository(db)
    criarClienteUseCase = CriarClienteUseCase(cliente_repository)
    
    cliente = await criarClienteUseCase.execute(cliente_data)

    return cliente
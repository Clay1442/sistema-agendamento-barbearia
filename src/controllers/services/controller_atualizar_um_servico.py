from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.schemas.servico_schema import ServicoUpdate
from src.use_case.service.atualizar_servico_use_case import AtualizarServicoUseCase
from src.repositories.servico_repository import ServicoRepository

router = APIRouter()

@router.put(
    "/{id}",
    tags=["Serviços"],
    summary="Atualizar um serviço existente",
    response_model=ServicoResponse
)

async def atualizar_um_servico(id: int, servico_data: ServicoUpdate, db: AsyncSession = Depends(get_db)):
    # Atualizar um serviço existente com as novas informações.

    servicoRepository = ServicoRepository(db)

    atualizarServicoUseCase = AtualizarServicoUseCase(servicoRepository)

    servico = await atualizarServicoUseCase.execute(id, servico_data)

    return servico
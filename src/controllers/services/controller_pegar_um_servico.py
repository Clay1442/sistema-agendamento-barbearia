from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.repositories.servico_repository import ServicoRepository
from src.use_case.service.pegar_servico_use_case import PegarServicoUseCase

router = APIRouter()

@router.get(
    "/",
    tags=["Serviços"],
    summary="Obter serviço da babearia", 
    response_model=ServicoResponse
)
async def pegar_um_servico(servico_id: int, db: AsyncSession = Depends(get_db)):
    # Retorna os detalhes de um serviço específico, identificado pelo seu ID.

    servicoRepository = ServicoRepository(db)

    pegarServicoUseCase = PegarServicoUseCase(servicoRepository)

    servico = await pegarServicoUseCase.execute(servico_id)

    return servico
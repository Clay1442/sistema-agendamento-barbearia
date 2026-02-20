from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.repositories.servico_repository import ServicoRepository
from src.services.pegar_servico_id_use_case import PegarServicoIdUseCase

router = APIRouter()

@router.get(
    "/",
    tags=["Serviços"],
    summary="Obter serviço da babearia", 
    response_model=ServicoResponse
)
async def pegar_servico_por_id(servico_id: int, db: AsyncSession = Depends(get_db)):
    # Retorna os detalhes de um serviço específico, identificado pelo seu ID.

    servicoRepository = ServicoRepository(db)

    pegarServicoIdUseCase = PegarServicoIdUseCase(servicoRepository)

    servico = await pegarServicoIdUseCase.execute(servico_id)

    return servico
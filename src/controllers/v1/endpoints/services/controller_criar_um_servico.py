from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.schemas.servico_schema import ServicoCreate
from src.repositories.servico_repository import ServicoRepository
from src.services.criar_servico_use_case import CriarServicoUseCase

router = APIRouter()

@router.post(
    "/",
    tags=["Serviços"],
    summary="Criar um novo serviço", 
    response_model=ServicoResponse
)
async def criar_um_servico(servico_data: ServicoCreate, db: AsyncSession = Depends(get_db)):
    # Criar um serviço com suas propriedades.

    servicoRepository = ServicoRepository(db)

    criarServicoUseCase = CriarServicoUseCase(servicoRepository)

    servico = await criarServicoUseCase.execute(servico_data)

    return servico
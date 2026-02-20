from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.schemas.servico_schema import ServicoResponse
from src.repositories.servico_repository import ServicoRepository
from src.services.deletar_servico_use_case import DeletarServicoUseCase

router = APIRouter()

@router.delete(
    "/",
    tags=["Serviços"],
    summary="Excluir um serviço da babearia", 
    response_model=None
)
async def deletar_um_servico(servico_id: int, db: AsyncSession = Depends(get_db)):
    # Deletar um serviço específico, identificado pelo seu ID.

    servicoRepository = ServicoRepository(db)

    deletarServicoUseCase = DeletarServicoUseCase(servicoRepository)

    servico = await deletarServicoUseCase.execute(servico_id)

    return servico
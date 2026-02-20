from src.repositories.servico_repository import ServicoRepository
from src.models.servico_model import ServicoModel
from src.schemas.servico_schema import ServicoBase
from fastapi import HTTPException

class CriarServicoUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository

    async def execute(self, servico_id: int) -> ServicoModel.id | None:

        servico = await self.servicoRepository.pegar_servico_id(servico_id)

        if not servico:
            raise HTTPException(tatus_code=404, detail="Servoço não encontrada")

        return servico
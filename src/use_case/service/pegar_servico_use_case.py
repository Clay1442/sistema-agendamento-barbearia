from src.repositories.servico_repository import ServicoRepository
from src.models.servico_model import ServicoModel
from fastapi import HTTPException

class PegarServicoUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository

    async def execute(self, servico_id: int) -> ServicoModel | None:

        servico = await self.servicoRepository.pegar_servico(servico_id)

        if not servico:
            raise HTTPException(status_code=404, detail="Serviço não encontrada")

        return servico
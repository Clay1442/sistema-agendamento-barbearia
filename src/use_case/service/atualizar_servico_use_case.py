from src.repositories.servico_repository import ServicoRepository
from src.models.servico_model import ServicoModel
from src.schemas.servico_schema import ServicoUpdate
from fastapi import HTTPException

class AtualizarServicoUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository
    
    async def execute(self, id: int, servico_data: ServicoUpdate) -> ServicoModel | None:

        servico = await self.servicoRepository.atualizar_servico(id, servico_data)

        if not servico:
            raise HTTPException(status_code=404, detail="Serviço não encontrado")
        return servico
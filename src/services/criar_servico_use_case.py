from src.repositories.servico_repository import ServicoRepository
from src.models.servico_model import ServicoModel
from src.schemas.servico_schema import ServicoCreate
from fastapi import HTTPException

class CriarServicoUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository

    async def execute(self, servico_data: ServicoCreate) -> ServicoModel | None:

        servico = await self.servicoRepository.criar_servico(servico_data)

        if not servico:
            raise HTTPException(status_code=409, detail="Não foi possível criar um novo serviço")

        return servico
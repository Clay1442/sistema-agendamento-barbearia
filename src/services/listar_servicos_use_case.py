from src.repositories.servico_repository import ServicoRepository
from src.models.servico_model import ServicoModel
from typing import List

class ListarServicosUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository

    async def execute(self) -> List[ServicoModel]:

        servicos = await self.servicoRepository.pegar_todos_servicos()

        return servicos
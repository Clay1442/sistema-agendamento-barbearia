from src.repositories.servico_repository import ServicoRepository
from fastapi import HTTPException

class DeletarServicoUseCase:
    def __init__(self, servicoRepository: ServicoRepository):
        self.servicoRepository = servicoRepository

    async def execute(self, servico_id: int) -> None:

        servico = await self.servicoRepository.pegar_servico(servico_id)

        if not servico:
            raise HTTPException(status_code=404, detail="Serviço não encontrada")

        await self.servicoRepository.deletar_servico(servico.id)

        return 
from typing import List
from src.repositories.cliente_repository import ClienteRepository
from src.models.cliente_model import ClienteModel

class ListarClientesUseCase:
    def __init__(self, clienteRepository: ClienteRepository):
        self.clienteRepository = clienteRepository

    async def execute(self) -> List[ClienteModel]:
        clientes = await self.clienteRepository.listar_clientes()
        return clientes
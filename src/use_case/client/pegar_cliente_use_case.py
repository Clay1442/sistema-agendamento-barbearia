from fastapi import HTTPException, status
from src.models.cliente_model import ClienteModel
from src.repositories.cliente_repository import ClienteRepository

class PegarClienteUseCase:
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository

    async def execute(self, cliente_id: int) -> ClienteModel:
        cliente = await self.cliente_repository.pegar_cliente(cliente_id)
        if not cliente:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
        return cliente
from fastapi import APIRouter, HTTPException
from src.repositories.cliente_repository import ClienteRepository

class DeletarClienteUseCase:
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository

    async def execute(self, cliente_id: int) -> None:
        cliente = await self.cliente_repository.pegar_cliente(cliente_id)
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        await self.cliente_repository.deletar_cliente(cliente_id)
        return



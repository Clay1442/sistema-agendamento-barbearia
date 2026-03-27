from src.repositories.cliente_repository import ClienteRepository
from src.models.cliente_model import ClienteModel
from src.schemas.cliente_schema import ClienteCreate
from fastapi import HTTPException

class CriarClienteUseCase:
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository

    async def execute(self, cliente_data: ClienteCreate) -> ClienteModel:
        # Verifica se já existe um cliente com o mesmo telefone
        cliente_existente = await self.cliente_repository.pegar_cliente_por_telefone(cliente_data.telefone)
        if cliente_existente:
            raise HTTPException(status_code=409, detail="Já existe um cliente com esse telefone")
        
        cliente = await self.cliente_repository.create_cliente(cliente_data)
        if not cliente:
            raise HTTPException(status_code=500, detail="Não foi possível criar um novo cliente")
        
        return cliente
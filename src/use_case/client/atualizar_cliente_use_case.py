from fastapi import HTTPException, status
from src.repositories.cliente_repository import ClienteRepository
from src.models.cliente_model import ClienteModel
from src.schemas.cliente_schema import ClienteUpdate

class AtualizarClienteUseCase:
    def __init__(self, clienteRepository: ClienteRepository):
        self.clienteRepository = clienteRepository
    
    async def execute(self, cliente_id: int, cliente_data: ClienteUpdate) -> ClienteModel:
        # Se o utilizador tentou atualizar o telefone, temos de verificar se o novo número já não pertence a outro cliente!
        if cliente_data.telefone:
            cliente_com_mesmo_numero = await self.clienteRepository.pegar_cliente_por_telefone(cliente_data.telefone)
            # Se achou alguém com esse número E não é o próprio cliente que estamos a atualizar
            if cliente_com_mesmo_numero and cliente_com_mesmo_numero.id != cliente_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="Este telefone já está a ser utilizado por outro cliente."
                )

        cliente_atualizado = await self.clienteRepository.atualizar_cliente(cliente_id, cliente_data)

        if not cliente_atualizado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Cliente não encontrado para atualização."
            )
            
        return cliente_atualizado
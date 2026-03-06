from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import delete
from src.models.cliente_model import ClienteModel
from src.schemas.cliente_schema import ClienteCreate, ClienteUpdate

class ClienteRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_cliente(self, cliente_data: ClienteCreate):
        novo_cliente = ClienteModel(**cliente_data.model_dump())
        self.db.add(novo_cliente)
        await self.db.commit() 
        await self.db.refresh(novo_cliente)
        return novo_cliente

    async def listar_clientes(self):
        query = select(ClienteModel)
        result = await self.db.execute(query)       
        return result.scalars().all()
    
    async def pegar_cliente(self, cliente_id: int):
        query = select(ClienteModel).where(ClienteModel.id == cliente_id)
        result = await self.db.execute(query)
        return result.scalars().first() # Retorna o primeiro que achar ou None

    async def pegar_cliente_por_telefone(self, telefone:str):
        query = select(ClienteModel).where(ClienteModel.telefone == telefone)
        result = await self.db.execute(query)
        return result.scalars().first() # Retorna o primeiro que achar ou None

    async def deletar_cliente(self, cliente_id: int):
        query = delete(ClienteModel).where(ClienteModel.id == cliente_id)
        await self.db.execute(query)
        await self.db.commit()
        return

    async def atualizar_cliente(self, cliente_id: int, cliente_data: ClienteUpdate):
        # Primeiro, pega o cliente existente
        # Isso é necessário para manter o ID e outros campos que não estão sendo atualizados
        cliente_existente = await self.pegar_cliente(cliente_id)    
        
        if not cliente_existente:
            return None
        
        update_data = cliente_data.model_dump(exclude_unset=True)
        # Atualiza os campos do cliente existente com os novos dados
        for key, value in update_data.items():
            setattr(cliente_existente, key, value)
        self.db.add(cliente_existente)        
        await self.db.commit()
        await self.db.refresh(cliente_existente)
        return cliente_existente    
        
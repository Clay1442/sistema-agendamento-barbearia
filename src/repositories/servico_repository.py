from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import delete
from src.models.servico_model import ServicoModel
from src.schemas.servico_schema import ServicoCreate, ServicoUpdate

class ServicoRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def criar_servico(self, servico_data: ServicoCreate):
        # Pega os dados validados do Pydantic (.model_dump()) e converte no Modelo do Banco
        novo_servico = ServicoModel(**servico_data.model_dump())
        
        # Adiciona na sessão e salva no banco
        self.db.add(novo_servico)
        await self.db.commit()
        
        await self.db.refresh(novo_servico)
        
        return novo_servico

    async def listar_servicos(self):
        # Constrói a query: SELECT * FROM servicos
        query = select(ServicoModel)
        
        # Executa a query de forma assíncrona
        result = await self.db.execute(query)
        
        # O .scalars().all() pega as linhas do banco e transforma numa lista de objetos Python
        return result.scalars().all()

    async def pegar_servico(self, servico_id: int):
        # Constrói a query: SELECT * FROM servicos WHERE id = ?
        query = select(ServicoModel).where(ServicoModel.id == servico_id)
        
        result = await self.db.execute(query)

        return result.scalars().first() # Retorna o primeiro que achar ou None
    
    async def deletar_servico(self, servico_id: int):
        # Constrói a query: DELETE * FROM servicos WHERE id = ?
        query = delete(ServicoModel).where(ServicoModel.id == servico_id)
        
        await self.db.execute(query)
        await self.db.commit()
        return

    async def atualizar_servico(self, servico_id: int, servico_data: ServicoUpdate):
        # Primeiro, pega o serviço existente
        # Isso é necessário para manter o ID e outros campos que não estão sendo atualizados
        servico_existente = await self.pegar_servico(servico_id)    
        
        if not servico_existente:
            return None
        
        update_data = servico_data.model_dump(exclude_unset=True)

        # Atualiza os campos do serviço existente com os novos dados
        for key, value in update_data.items():
            setattr(servico_existente, key, value)

        self.db.add(servico_existente)    
        await self.db.commit()
        await self.db.refresh(servico_existente)

        return servico_existente
    
    
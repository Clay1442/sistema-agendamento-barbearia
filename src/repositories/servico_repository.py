from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.servico_model import ServicoModel
from src.schemas.servico_schema import ServicoCreate

class ServicoRepository:
    
    async def get_all(self, db: AsyncSession):
        # Constrói a query: SELECT * FROM servicos
        query = select(ServicoModel)
        
        # Executa a query de forma assíncrona
        result = await db.execute(query)
        
        # O .scalars().all() pega as linhas do banco e transforma numa lista de objetos Python
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, servico_id: int):
        # Constrói a query: SELECT * FROM servicos WHERE id = ?
        query = select(ServicoModel).filter(ServicoModel.id == servico_id)
        
        result = await db.execute(query)
        return result.scalars().first() # Retorna o primeiro que achar ou None

    async def create(self, db: AsyncSession, servico_data: ServicoCreate):
        # Pega os dados validados do Pydantic (.model_dump()) e converte no Modelo do Banco
        novo_servico = ServicoModel(**servico_data.model_dump())
        
        # Adiciona na sessão e salva no banco
        db.add(novo_servico)
        await db.commit()
        
        # Atualiza o objeto para pegar o ID que o banco gerou
        await db.refresh(novo_servico)
        return novo_servico
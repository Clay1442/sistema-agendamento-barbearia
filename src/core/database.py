from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# URL de conexão com SQLite (driver aiosqlite para async)
DATABASE_URL = "sqlite+aiosqlite:///./barbearia.db"

# Cria o motor do banco de dados
engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    connect_args={"check_same_thread": False} # Necessário apenas para SQLite
)

# Cria a fábrica de sessões (cada request ganha uma)
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

# Classe base para os Models (Tabelas) herdarem
class Base(DeclarativeBase):
    pass

# Dependência para injetar o banco nas rotas
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
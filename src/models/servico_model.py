from sqlalchemy import Column, Integer, String, Float
from src.core.database import Base

class ServicoModel(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
    duracao_minutos = Column(Integer, nullable=False)
        
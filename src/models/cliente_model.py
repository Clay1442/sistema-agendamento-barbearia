from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class ClienteModel(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)  
    nome = Column(String, nullable=False)
    telefone = Column(String, unique=True, index=True, nullable=False)

    #Relacionamento com agendamento
    agendamentos = relationship("AgendamentoModel", back_populates="cliente")

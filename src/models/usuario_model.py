from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from src.core.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False) # Armazena o hash da senha
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Usuario {self.email} - {self.perfil}>"
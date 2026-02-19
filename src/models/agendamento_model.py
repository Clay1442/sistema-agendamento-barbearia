from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.enums import StatusAgendamento

class AgendamentoModel(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data_horario = Column(DateTime, nullable=False)
    status = Column(String, default=StatusAgendamento.StatusAgendamento.AGENDADO.value)  

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    servico_id = Column(Integer, ForeignKey("servicos.id"))

    # Relacionamentos
    cliente = relationship("ClienteModel", back_populates="agendamentos")
    servico = relationship("ServicoModel")





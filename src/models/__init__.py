from src.models.usuario_model import UsuarioModel
from src.models.servico_model import ServicoModel
from src.models.cliente_model import ClienteModel
from src.models.agendamento_model import AgendamentoModel

# Opcional, mas útil: expor uma lista de todos os modelos
__all__ = [
    "UsuarioModel",
    "ServicoModel",
    "ClienteModel",
    "AgendamentoModel",
]
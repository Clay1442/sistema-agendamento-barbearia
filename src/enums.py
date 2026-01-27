from enum import Enum


class StatusAgendamento(str, Enum):
    """Enum para tipos de status de agendamento."""
    AGENDADO = "agendado"
    CONFIRMADO = "confirmado"
    CANCELADO = "cancelado"
    CONCLUIDO = "concluido"
    NAO_COMPARECEU = "nao_compareceu"

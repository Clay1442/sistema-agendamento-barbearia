from fastapi import APIRouter

from src.controllers.v1.endpoints.controller_listar_todos_servicos import router as listar_todos_servicos
from src.controllers.v1.endpoints.controller_pegar_servico_id import router as pegar_servico_por_id

router = APIRouter()

router.include_router(listar_todos_servicos, prefix="/api/v1/servicos")
router.include_router(pegar_servico_por_id, prefix="/api/v1/servicos/{servico_id}")

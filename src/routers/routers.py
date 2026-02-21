from fastapi import APIRouter

from src.controllers.services.controller_listar_todos_servicos import router as listar_todos_servicos
from src.controllers.services.controller_pegar_um_servico import router as pegar_um_servico
from src.controllers.services.controller_criar_um_servico import router as criar_um_servico
from src.controllers.services.controller_deletar_um_servico import router as deletar_um_servico

router = APIRouter()

router.include_router(criar_um_servico, prefix="/api/v1/servicos/criar")
router.include_router(pegar_um_servico, prefix="/api/v1/servicos/pegar/{servico_id}")
router.include_router(deletar_um_servico, prefix="/api/v1/servicos/deletar/{servico_id}")
router.include_router(listar_todos_servicos, prefix="/api/v1/servicos/listar")


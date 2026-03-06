from fastapi import APIRouter

# Importando os routers dos Serviços
from src.controllers.services.controller_listar_todos_servicos import router as listar_todos_servicos
from src.controllers.services.controller_pegar_um_servico import router as pegar_um_servico
from src.controllers.services.controller_criar_um_servico import router as criar_um_servico
from src.controllers.services.controller_deletar_um_servico import router as deletar_um_servico
from src.controllers.services.controller_atualizar_um_servico import router as atualizar_um_servico

# Importando os routers dos Clientes
from src.controllers.clients.controller_cadastrar_um_cliente import router as cadastrar_um_cliente
from src.controllers.clients.controller_listar_todos_clientes import router as listar_todos_clientes
from src.controllers.clients.controller_pegar_cliente import router as pegar_um_cliente
from src.controllers.clients.controller_deletar_cliente import router as deletar_um_cliente
from src.controllers.clients.controller_atualizar_um_cliente import router as atualizar_um_cliente

router = APIRouter()

#Routers Serviços
router.include_router(criar_um_servico, prefix="/servicos")
router.include_router(listar_todos_servicos, prefix="/servicos")
router.include_router(pegar_um_servico, prefix="/servicos")
router.include_router(deletar_um_servico, prefix="/servicos")
router.include_router(atualizar_um_servico, prefix="/servicos")

#Routers Clientes
router.include_router(cadastrar_um_cliente, prefix="/clientes")
router.include_router(listar_todos_clientes, prefix="/clientes")
router.include_router(pegar_um_cliente, prefix="/clientes")
router.include_router(deletar_um_cliente, prefix="/clientes")
router.include_router(atualizar_um_cliente, prefix="/cliente")

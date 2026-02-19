from fastapi import FastAPI
# Importa o roteador que acabamos de criar
from src.api.v1.endpoints import servicos

app = FastAPI(
    title="API da Barbearia",
    description="Sistema de Agendamento",
    version="1.0.0"
)

# Conecta as rotas de serviços na aplicação principal
app.include_router(
    servicos.router, 
    prefix="/api/v1/servicos", 
    tags=["Serviços"]
)


@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Barbearia!"}
from fastapi import FastAPI
from src.routers.routers import router as routers

app = FastAPI(
    title="API da Barbearia",
    description="Sistema de Agendamento",
    version="1.0.0"
)

app.include_router(routers)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Barbearia!"}
import asyncio
from datetime import datetime, timedelta
from src.core.database import SessionLocal, engine
from src.models.usuario_model import UsuarioModel
from src.models.servico_model import ServicoModel
from src.models.cliente_model import ClienteModel
from src.models.agendamento_model import AgendamentoModel
from sqlalchemy import text

async def popular_banco():
    print("🌱 Iniciando o processo de Seed (Semeadura)...")
    
    # Cria uma sessão com o banco
    async with SessionLocal() as session:
        try:
            # 1. Limpar dados antigos (Ordem importa para não quebrar FK)
            # Deletamos filhos (agendamentos) antes dos pais (clientes/servicos)
            print("🧹 Limpando tabelas antigas...")
            await session.execute(text("DELETE FROM agendamentos"))
            await session.execute(text("DELETE FROM servicos"))
            await session.execute(text("DELETE FROM clientes"))
            await session.execute(text("DELETE FROM usuarios"))
            
          # Tenta resetar os IDs, mas ignora se a tabela não existir
            try:
                await session.execute(text("DELETE FROM sqlite_sequence"))
            except Exception:
                pass # Tabela ainda não existe, vida que segue

            # 2. Criar Usuário Admin
            print("👤 Criando Admin...")
            admin = UsuarioModel(
                nome="Mestre Barbeiro",
                email="admin@barbearia.com",
                senha_hash="senha_segura_123", # Em prod, isso seria hash!
            )
            session.add(admin)

            # 3. Criar Serviços (O Cardápio)
            print("✂️ Criando Serviços...")
            corte = ServicoModel(nome="Corte Degradê", preco=45.00, duracao_minutos=45)
            barba = ServicoModel(nome="Barba Terapia", preco=35.00, duracao_minutos=30)
            completo = ServicoModel(nome="Cabelo e Barba", preco=70.00, duracao_minutos=75)
            
            session.add_all([corte, barba, completo])
            # Precisamos do flush para gerar os IDs desses objetos antes de usar no agendamento
            await session.flush() 

            # 4. Criar Clientes
            print("👥 Criando Clientes...")
            cliente_joao = ClienteModel(nome="João Silva", telefone="11999999999")
            cliente_maria = ClienteModel(nome="Maria Souza", telefone="11888888888")
            
            session.add_all([cliente_joao, cliente_maria])
            await session.flush() # Gera os IDs dos clientes

            # 5. Criar Agendamentos (O Teste de Fogo das Relações)
            print("📅 Criando Agendamentos...")
            
            # Agendamento 1: João vai cortar cabelo amanhã às 10h
            data_amanha = datetime.now() + timedelta(days=1)
            data_amanha = data_amanha.replace(hour=10, minute=0, second=0, microsecond=0)

            agendamento1 = AgendamentoModel(
                cliente_id=cliente_joao.id,  # Usa o ID gerado acima
                servico_id=corte.id,         # Usa o ID gerado acima
                data_horario=data_amanha,
                status="agendado",
            )

            # Agendamento 2: Maria vai fazer barba (exemplo) depois de amanhã
            agendamento2 = AgendamentoModel(
                cliente_id=cliente_maria.id,
                servico_id=barba.id,
                data_horario=data_amanha + timedelta(days=1),
                status="confirmado"
            )

            session.add_all([agendamento1, agendamento2])
            
            # Salva tudo de verdade
            await session.commit()
            print("✅ Banco populado com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao popular banco: {e}")
            await session.rollback() # Desfaz tudo se der erro

    # Fecha conexão do motor
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(popular_banco())
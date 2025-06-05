import streamlit as st
from app.services.reserva_service import ReservaService
from app.Model.database import Database

from app.view.telaInicio import tela_inicio
from app.view.telaUsuario import tela_usuario
from app.view.telaQuarto import tela_quarto
from app.view.telaReserva import tela_reserva
from app.view.telaEditarReserva import tela_editar_reserva
from app.view.telaHistoricoReserva import tela_historico_reserva


db = Database()
db.connect()
reserva_service = ReservaService(db)

# Sidebar para navegação
st.sidebar.title("Menu")
tela = st.sidebar.radio(
    "Escolha uma tela:",
    [
        "Início",
        "Criar Usuário",
        "Criar Quarto",
        "Criar Reserva",
        "Editar Reserva",
        "Histórico de Reservas"
    ]
)

# Tela Início
if tela == "Início":
    tela_inicio(db, reserva_service)

# Tela Criar Usuário
elif tela == "Criar Usuário":
    tela_usuario(reserva_service, db)

# Tela Criar Quarto
elif tela == "Criar Quarto":
    tela_quarto(reserva_service, db)

# Tela Criar Reserva
elif tela == "Criar Reserva":
    tela_reserva(db, reserva_service)

# Tela Editar Reserva
elif tela == "Editar Reserva":
    tela_editar_reserva(db)

# Tela Histórico de Reservas
elif tela == "Histórico de Reservas":
    tela_historico_reserva(db)

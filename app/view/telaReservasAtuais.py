import streamlit as st
import pandas as pd

def tela_reservas_atuais(reserva_service):
    st.title("Reservas Atuais")
    reservations = reserva_service.get_all_reservations()
    if reservations:
        df = pd.DataFrame(reservations)
        df.columns = ["ID da Reserva", "Hóspede", "Quarto", "Check-in", "Check-out"]
        st.table(df)
    else:
        st.info("Nenhuma reserva encontrada.")
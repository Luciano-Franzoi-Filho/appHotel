import streamlit as st
import pandas as pd

def tela_buscar_por_data(db):
    st.title("Buscar Reservas por Data")
    data_busca = st.date_input("Selecione a data para buscar reservas", key="busca_data")
    if st.button("Buscar por Data"):
        reservas_data = db.execute_query("""
            SELECT r.id, h.nome, q.numero, r.data_entrada, r.data_saida
            FROM reservas r
            JOIN hospedes h ON r.hospede_id = h.id
            JOIN quartos q ON r.quarto_id = q.id
            WHERE r.data_entrada <= ? AND r.data_saida >= ?
        """, (str(data_busca), str(data_busca)))
        if reservas_data:
            df_reservas_data = pd.DataFrame(reservas_data, columns=["ID", "Hóspede", "Quarto", "Check-in", "Check-out"])
            st.table(df_reservas_data)
        else:
            st.info("Nenhuma reserva encontrada para esta data.")
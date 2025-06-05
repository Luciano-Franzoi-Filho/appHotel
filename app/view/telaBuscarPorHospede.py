import streamlit as st
import pandas as pd

def tela_buscar_por_hospede(db):
    st.title("Buscar Reservas por Hóspede")
    hospedes_busca = db.fetch_hospedes()
    if hospedes_busca:
        opcoes_hospede = {h[1]: h[0] for h in hospedes_busca}
        hospede_busca = st.selectbox("Selecione o hóspede", list(opcoes_hospede.keys()), key="busca_hospede")
        if st.button("Buscar Reservas"):
            reservas_hospede = db.execute_query("""
                SELECT r.id, h.nome, q.numero, r.data_entrada, r.data_saida
                FROM reservas r
                JOIN hospedes h ON r.hospede_id = h.id
                JOIN quartos q ON r.quarto_id = q.id
                WHERE h.id = ?
            """, (opcoes_hospede[hospede_busca],))
            if reservas_hospede:
                df_reservas_hospede = pd.DataFrame(reservas_hospede, columns=["ID", "Hóspede", "Quarto", "Check-in", "Check-out"])
                st.table(df_reservas_hospede)
            else:
                st.info("Nenhuma reserva encontrada para este hóspede.")
    else:
        st.info("Nenhum hóspede cadastrado.")
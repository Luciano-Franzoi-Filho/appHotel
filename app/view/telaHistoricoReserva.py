import streamlit as st
import pandas as pd

def tela_historico_reserva(db):
    st.title("Histórico e Busca de Reservas")

    st.subheader("Buscar por Hóspede")
    hospedes_busca = db.fetch_hospedes()
    if hospedes_busca:
        opcoes_hospede = {h[1]: h[0] for h in hospedes_busca}
        hospede_hist = st.selectbox("Selecione o hóspede", list(opcoes_hospede.keys()), key="hist_hospede")
        if st.button("Ver Histórico"):
            historico = db.execute_query("""
                SELECT r.id, q.numero, r.data_entrada, r.data_saida
                FROM reservas r
                JOIN quartos q ON r.quarto_id = q.id
                WHERE r.hospede_id = ?
            """, (opcoes_hospede[hospede_hist],))
            if historico:
                df_hist = pd.DataFrame(historico, columns=["ID Reserva", "Quarto", "Check-in", "Check-out"])
                st.table(df_hist)
            else:
                st.info("Nenhum histórico encontrado para este hóspede.")
    else:
        st.info("Nenhum hóspede cadastrado.")

    st.markdown("---")

    st.subheader("Buscar por Data")
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

    st.markdown("---")

    st.subheader("Buscar por Nome do Hóspede")
    nome_busca = st.text_input("Digite o nome (ou parte do nome) do hóspede para buscar reservas")
    if st.button("Buscar por Nome"):
        if nome_busca.strip():
            reservas_nome = db.execute_query("""
                SELECT r.id, h.nome, q.numero, r.data_entrada, r.data_saida
                FROM reservas r
                JOIN hospedes h ON r.hospede_id = h.id
                JOIN quartos q ON r.quarto_id = q.id
                WHERE h.nome LIKE ?
            """, (f"%{nome_busca.strip()}%",))
            if reservas_nome:
                df_reservas_nome = pd.DataFrame(reservas_nome, columns=["ID", "Hóspede", "Quarto", "Check-in", "Check-out"])
                st.table(df_reservas_nome)
            else:
                st.info("Nenhuma reserva encontrada para este nome.")
        else:
            st.warning("Digite um nome para buscar.")
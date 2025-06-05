import streamlit as st
import pandas as pd
import sqlite3

def tela_reserva(db, reserva_service):
    st.title("Reservas")

    st.subheader("Criar Nova Reserva")
    hospedes = db.execute_query("SELECT id, nome FROM hospedes")
    quartos = db.execute_query("SELECT id, numero FROM quartos WHERE status = 'disponível'")
    hospede_opcoes = {nome: id for id, nome in hospedes}
    quarto_opcoes = {str(numero): id for id, numero in quartos}
    with st.form(key='create_reservation_form'):
        hospede_nome = st.selectbox("Selecione o Hóspede", list(hospede_opcoes.keys()))
        quarto_numero = st.selectbox("Selecione o Quarto", list(quarto_opcoes.keys()))
        data_entrada = st.date_input("Data de Check-in")
        data_saida = st.date_input("Data de Check-out")
        submit_reservation = st.form_submit_button("Criar Reserva")
        if submit_reservation:
            try:
                user_id = hospede_opcoes[hospede_nome]
                room_id = quarto_opcoes[quarto_numero]
                reserva_service.create_reservation(user_id, room_id, data_entrada, data_saida)
                st.success("Reserva criada com sucesso!")
            except sqlite3.IntegrityError:
                st.error("Este quarto já está reservado para o período selecionado ou está ocupado. Por favor, escolha outro quarto.")
            except KeyError:
                st.error("O quarto selecionado não está disponível. Atualize a página e tente novamente.")

    st.subheader("Reservas Atuais")
    reservations = reserva_service.get_all_reservations()
    if reservations:
        df = pd.DataFrame(reservations)
        df.columns = ["ID da Reserva", "Hóspede", "Quarto", "Check-in", "Check-out"]
        st.table(df)
    else:
        st.info("Nenhuma reserva encontrada.")
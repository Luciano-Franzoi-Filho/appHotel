import streamlit as st
import pandas as pd
import sqlite3

def tela_quarto(reserva_service, db):
    st.title("Quartos")

    st.subheader("Cadastrar Novo Quarto")
    with st.form(key='create_room_form'):
        numero = st.number_input("Número do Quarto", min_value=1)
        tipo = st.selectbox("Tipo de quarto", ["Simples", "Duplo", "Suite"])
        submit_room = st.form_submit_button("Criar Quarto")
        if submit_room:
            try:
                reserva_service.create_room(numero, tipo)
                st.success("Quarto criado com sucesso!")
            except sqlite3.IntegrityError:
                st.error("Já existe um quarto com esse número. Por favor, escolha outro número.")

    st.subheader("Quartos Cadastrados")
    quartos_lista = db.fetch_quartos()
    if quartos_lista:
        df_quartos = pd.DataFrame(quartos_lista, columns=["ID", "Número", "Tipo", "Status"])
        st.table(df_quartos)
    else:
        st.info("Nenhum quarto cadastrado.")
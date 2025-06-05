import streamlit as st
import pandas as pd

def tela_usuario(reserva_service, db):
    st.title("Usuários (Hóspedes)")

    st.subheader("Cadastrar Novo Usuário")
    with st.form(key='create_user_form'):
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        submit_user = st.form_submit_button("Criar")
        if submit_user:
            reserva_service.create_user(nome, cpf, telefone)
            st.success("Usuário criado com sucesso!")

    st.subheader("Hóspedes Cadastrados")
    hospedes_lista = db.fetch_hospedes()
    if hospedes_lista:
        df_hospedes = pd.DataFrame(hospedes_lista, columns=["ID", "Nome", "CPF", "Telefone"])
        st.table(df_hospedes)
    else:
        st.info("Nenhum hóspede cadastrado.")
import streamlit as st
import pandas as pd

def tela_lista_hospedes(db):
    st.title("Lista de Hóspedes")
    hospedes_lista = db.fetch_hospedes()
    if hospedes_lista:
        df_hospedes = pd.DataFrame(hospedes_lista, columns=["ID", "Nome", "CPF", "Telefone"])
        st.table(df_hospedes)
    else:
        st.info("Nenhum hóspede cadastrado.")
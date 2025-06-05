import streamlit as st
import pandas as pd

def tela_lista_quartos(db):
    st.title("Lista de Quartos")
    quartos_lista = db.fetch_quartos()
    if quartos_lista:
        df_quartos = pd.DataFrame(quartos_lista, columns=["ID", "Número", "Tipo", "Status"])
        st.table(df_quartos)
    else:
        st.info("Nenhum quarto cadastrado.")
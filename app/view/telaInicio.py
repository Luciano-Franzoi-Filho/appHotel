import streamlit as st
import pandas as pd

def tela_inicio(db, reserva_service):
    st.title("Painel Inicial")
    st.subheader("Quartos")
    quartos_lista = db.fetch_quartos()
    if quartos_lista:
        df_quartos = pd.DataFrame(quartos_lista, columns=["ID", "Número", "Tipo", "Status"])
        st.table(df_quartos)
    else:
        st.info("Nenhum quarto cadastrado.")

    st.subheader("Reservas Atuais")
    reservations = reserva_service.get_all_reservations()
    if reservations:
        df = pd.DataFrame(reservations)
        df.columns = ["ID da Reserva", "Hóspede", "Quarto", "Check-in", "Check-out"]
        st.table(df)
    else:
        st.info("Nenhuma reserva encontrada.")

    st.subheader("Hóspedes")
    hospedes_lista = db.fetch_hospedes()
    if hospedes_lista:
        df_hospedes = pd.DataFrame(hospedes_lista, columns=["ID", "Nome", "CPF", "Telefone"])
        st.table(df_hospedes)
    else:
        st.info("Nenhum hóspede cadastrado.")

    st.subheader("Check-out Rápido")
    reservas_checkout = db.fetch_reservas()
    if reservas_checkout:
        opcoes_checkout = {f"{r[0]} - {r[1]} - Quarto {r[2]}": (r[0], r[2]) for r in reservas_checkout}
        reserva_checkout = st.selectbox("Selecione a reserva para check-out", list(opcoes_checkout.keys()), key="checkout_inicio")
        if st.button("Fazer Check-out", key="btn_checkout_inicio"):
            reserva_id, quarto_numero = opcoes_checkout[reserva_checkout]
            with db.connection:
                db.connection.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
                db.connection.execute("UPDATE quartos SET status = 'disponível' WHERE numero = ?", (quarto_numero,))
            st.success("Check-out realizado e quarto liberado!")
    else:
        st.info("Nenhuma reserva para check-out.")

import streamlit as st

def tela_checkout(db):
    st.title("Check-out")
    reservas_checkout = db.fetch_reservas()
    if reservas_checkout:
        opcoes_checkout = {f"{r[0]} - {r[1]} - Quarto {r[2]}": (r[0], r[2]) for r in reservas_checkout}
        reserva_checkout = st.selectbox("Selecione a reserva para check-out", list(opcoes_checkout.keys()), key="checkout")
        if st.button("Fazer Check-out"):
            reserva_id, quarto_numero = opcoes_checkout[reserva_checkout]
            with db.connection:
                db.connection.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
                db.connection.execute("UPDATE quartos SET status = 'disponível' WHERE numero = ?", (quarto_numero,))
            st.success("Check-out realizado e quarto liberado!")
    else:
        st.info("Nenhuma reserva para check-out.")
import streamlit as st

def tela_cancelar_reserva(db):
    st.title("Cancelar Reserva")
    reservas_cancel = db.fetch_reservas()
    if reservas_cancel:
        opcoes_cancel = {f"{r[0]} - {r[1]} - Quarto {r[2]}": r[0] for r in reservas_cancel}
        reserva_cancelada = st.selectbox("Selecione a reserva para cancelar", list(opcoes_cancel.keys()), key="cancelar")
        if st.button("Cancelar Reserva"):
            reserva_id = opcoes_cancel[reserva_cancelada]
            with db.connection:
                db.connection.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
                db.connection.execute(
                    "UPDATE quartos SET status = 'disponível' WHERE id = (SELECT quarto_id FROM reservas WHERE id = ?)", 
                    (reserva_id,)
                )
            st.success("Reserva cancelada com sucesso!")
    else:
        st.info("Nenhuma reserva para cancelar.")
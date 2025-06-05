import streamlit as st
import pandas as pd

def tela_editar_reserva(db):
    st.title("Editar/Cancelar/Check-out de Reservas")
    reservas = db.fetch_reservas()
    if not reservas:
        st.info("Nenhuma reserva encontrada.")
        return

    opcoes = {f"{r[0]} - {r[1]} - Quarto {r[2]}": r for r in reservas}
    selecao = st.selectbox("Selecione a reserva", list(opcoes.keys()), key="editar_reserva")
    reserva = opcoes[selecao]
    reserva_id, hospede_nome, quarto_numero, data_entrada, data_saida = reserva

    st.markdown(f"**Hóspede:** {hospede_nome}  \n**Quarto:** {quarto_numero}  \n**Check-in:** {data_entrada}  \n**Check-out:** {data_saida}")

    st.subheader("Editar Datas da Reserva")
    nova_data_entrada = st.date_input("Nova Data de Check-in", key="edit_in", value=pd.to_datetime(data_entrada))
    nova_data_saida = st.date_input("Nova Data de Check-out", key="edit_out", value=pd.to_datetime(data_saida))
    if st.button("Salvar Alterações"):
        with db.connection:
            db.connection.execute(
                "UPDATE reservas SET data_entrada = ?, data_saida = ? WHERE id = ?",
                (str(nova_data_entrada), str(nova_data_saida), reserva_id)
            )
        st.success("Reserva atualizada com sucesso!")

    st.subheader("Cancelar Reserva")
    if st.button("Cancelar Reserva"):
        with db.connection:
            db.connection.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
            db.connection.execute("UPDATE quartos SET status = 'disponível' WHERE numero = ?", (quarto_numero,))
        st.success("Reserva cancelada e quarto liberado!")

    st.subheader("Check-out")
    if st.button("Fazer Check-out"):
        with db.connection:
            db.connection.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
            db.connection.execute("UPDATE quartos SET status = 'disponível' WHERE numero = ?", (quarto_numero,))
        st.success("Check-out realizado e quarto liberado!")
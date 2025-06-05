class ReservaService:
    def __init__(self, db):
        self.db = db

    def create_user(self, nome, cpf, telefone):
        from app.Model.hospede import Hospede
        hospede = Hospede(nome, cpf, telefone)
        self.db.insert_hospede(hospede)

    def create_room(self, numero, tipo):
        from app.Model.quarto import Quarto
        quarto = Quarto(numero, tipo)
        self.db.insert_quarto(quarto)

    def create_reservation(self, hospede_id, quarto_id, data_entrada, data_saida):
        from app.Model.reserva import Reserva
        reserva = Reserva(None, hospede_id, quarto_id, data_entrada, data_saida)
        self.db.insert_reserva(reserva)

    def get_reservations(self):
        return self.db.fetch_reservas()

    def get_rooms(self):
        return self.db.fetch_quartos()

    def get_users(self):
        return self.db.fetch_hospedes()
    
    def get_all_reservations(self):
        query = """
            SELECT r.id, h.nome, q.numero, r.data_entrada, r.data_saida
            FROM reservas r
            JOIN hospedes h ON r.hospede_id = h.id
            JOIN quartos q ON r.quarto_id = q.id
        """
        results = self.db.execute_query(query)
        reservas = []
        for row in results:
            reserva = {
                "id": row[0],
                "hospede_nome": row[1],
                "quarto_numero": row[2],
                "data_entrada": row[3],
                "data_saida": row[4]
            }
            reservas.append(reserva)
        return reservas    
class ReservaController:
    def __init__(self, reserva_service):
        self.reserva_service = reserva_service

    def create_reservation(self, hospede_data, quarto_data, data_entrada, data_saida):
        hospede = self.reserva_service.create_user(hospede_data)
        quarto = self.reserva_service.create_room(quarto_data)
        reserva = self.reserva_service.create_reservation(hospede, quarto, data_entrada, data_saida)
        return reserva

    def get_reservations(self):
        return self.reserva_service.get_all_reservations()
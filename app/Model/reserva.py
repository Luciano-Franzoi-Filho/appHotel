class Reserva:
    def __init__(self, id, hospede_id, quarto_id, data_entrada, data_saida):
        self.id = id
        self.hospede_id = hospede_id
        self.quarto_id = quarto_id
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def __str__(self):
        return f'Reserva ID: {self.id}, Hóspede ID: {self.hospede_id}, Quarto ID: {self.quarto_id}, Data de Entrada: {self.data_entrada}, Data de Saída: {self.data_saida}'
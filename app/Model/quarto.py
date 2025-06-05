class Quarto:
    def __init__(self, numero, tipo, status='disponível'):
        self.numero = numero
        self.tipo = tipo
        self.status = status

    def alterar_status(self, novo_status):
        self.status = novo_status

    def __str__(self):
        return f"Quarto {self.numero} - Tipo: {self.tipo} - Status: {self.status}"
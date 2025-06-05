class Hospede:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def __repr__(self):
        return f"Hospede(nome={self.nome}, cpf={self.cpf}, telefone={self.telefone})"
class Cliente:
    def __init__(self, cpf, nome, email, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco # Espera um dicionário ou objeto endereço

    def to_string(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Email: {self.email}"
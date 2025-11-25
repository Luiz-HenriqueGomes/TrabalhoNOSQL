class Produto:
    def __init__(self, nome, descricao, preco_unitario, estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque # Espera um dicionário com qtde, etc.

    def to_string(self):
        qtde = self.estoque.get('quantidade', 0)
        return f"Produto: {self.nome} | Preço: R$ {self.preco_unitario} | Estoque: {qtde}"
class Venda:
    def __init__(self, data_venda, valor_total, cliente_id, itens):
        self.data_venda = data_venda
        self.valor_total = valor_total
        self.cliente_id = cliente_id
        self.itens = itens

    def to_string(self):
        return f"Venda em: {self.data_venda} | Total: R$ {self.valor_total} | Itens: {len(self.itens)}"
    
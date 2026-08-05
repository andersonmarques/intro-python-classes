from item import Item
# from cliente_ import Cliente - evitar importação circular
from tipo_pagamento import Tipo_Pagamento

class Pedido:
    def __init__(self, tipo_pagamento: Tipo_Pagamento):
        # self.cliente = cliente
        self.itens : list[Item] = []
        self.tipo_pagamento = tipo_pagamento

    def add_item(self, item: Item):
        self.itens.append(item)

    def total(self):
        return sum(item.produto.preco * item.quant for item in self.itens)

    def __str__(self):
        itens_str = "\n".join(str(item) for item in self.itens)
        return f"Pedido do cliente: {self.cliente}\nItens:\n{itens_str}\nTotal: R${self.total():.2f}\nTipo de Pagamento: {self.tipo_pagamento}"
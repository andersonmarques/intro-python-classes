from produto import Produto

class Item:
    def __init__(self, produto: Produto, quant: float):
        self.produto = produto
        self.quant = quant

    def __str__(self):
        return f"{self.produto} - R${self.quant:.2f}"
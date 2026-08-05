class Produto:

    def __init__(self, nome_local, preco_local, quant_estoque_local):
        self.nome = nome_local
        self.preco = preco_local
        self.quant_estoque = quant_estoque_local

    def __str__(self): # \n \t
        return f"Produto: {self.nome}, \
                Preço: R${self.preco:.2f}, \
                Quantidade em Estoque: {self.quant_estoque}"
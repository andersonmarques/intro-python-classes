class Produto:

    def __init__(self, nome:str, preco:float, quant_estoque:int):
        self.nome = nome
        self.preco = preco
        self.quant_estoque = quant_estoque

    def __str__(self): # \n \t
        return f"Produto: {self.nome}, \
                Preço: R${self.preco:.2f}, \
                Quantidade em Estoque: {self.quant_estoque}"
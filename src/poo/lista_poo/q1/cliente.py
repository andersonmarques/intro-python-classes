from pedido import Pedido

class Cliente:
    def __init__(self, nome: str, cpf: str = ""):
        self.nome = nome
        self.cpf = cpf
        self.pedidos :list[Pedido] = []

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

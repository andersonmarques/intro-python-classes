from pedido import Pedido

class Cliente:
    def __init__(self, 
                 nome      : str, 
                 cpf       : str = "",
                 endereco  : str = "",
                 cep       : str = "",
                 categoria : str = "",
                 sexo      : str = "f"
                 ):
        self.erro = ""
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.cep = cep
        self.categoria = categoria
        self.sexo = sexo        
        self.pedidos :list[Pedido] = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        if len(nome) == 0:
            self.erro = 'O campo "nome" é obrigatório.'
        else:
            self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf:str):
        if len(cpf) == 0:
            self.erro = 'O campo "cpf" é obrigatório.'
        else:
            self.__cpf = cpf

    def __str__(self):
        return f"{self.nome}; {self.cpf}"

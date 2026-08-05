class Pessoa:
    def __init__(self, nome, idade):
        # inicializa o objeto Pessoa
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome},Idade: {self.idade}"

#refencia para o objeto Pessoa
pessoa_david = Pessoa("David", 19) # __init__() é chamado automaticamente
print(pessoa_david)  # chama o método __str__() do objeto pessoa_david
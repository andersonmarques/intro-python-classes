class Contato:
    # Especificadores de acesso: 
    # public    : se nao tiver _ o atributo é publico
    # private   : se tiver __ (2 _) o atributo é privado
    # protected : se tiver _ (1 _) o atributo é protegido
    # 
    # protected: só podem ser acessados pelas classes que herdam 
    # da classe pai, ou seja, pelas classes filhas.

    def __init__(self, nome: str, telefone: int, email: str | None = None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.erro = None

    @property
    def nome(self) -> str: # equivale ao getNome()
        return self.__nome

    @nome.setter
    def nome(self, nome: str): # equivale ao setNome()
        if nome == "":
            # raise ValueError("O nome não pode ser vazio.")
            self.erro = "O nome não pode ser vazio."
        else:
            self.__nome = nome

    @property
    def telefone(self) -> int: # equivale ao getTelefone()
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int): # equivale ao setTelefone()
        self.__telefone = telefone

    @property
    def email(self) -> str | None: # equivale ao getEmail()
        return self.__email

    @email.setter
    def email(self, email: str | None): # equivale ao setEmail()
        if email is not None and "@" not in email:
            raise ValueError("O email deve conter o caractere '@'.")    
        else:
            self.__email = email

    def __str__(self):
        return f"Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}"
from contato import Contato

class Agenda:
    def __init__(self):
        self.contatos :list[Contato] = []

    def pesquisar_por_numero(self, numero:int) -> Contato | None:
        '''
        Pesquisa um contato pelo número de telefone.
        Retorna o contato correspondente se encontrado, 
        caso contrário retorna None.
        
        Parametro:
        * numero (int): O número de telefone a ser pesquisado.
        '''
        for contato in self.contatos:
            if contato.telefone == numero:
                return contato
        else:
            return None
            
    def salvar_contato_agenda(self, contato: Contato):
        '''
        Salva um contato na agenda.
        Parametro:
        * contato (Contato): O contato a ser salvo na agenda.
        '''
        self.contatos.append(contato)

    def pesquisar_todos_contatos(self):
        '''
        Pesquisa todos os contatos na agenda.
        '''
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
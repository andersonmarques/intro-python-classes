from contato import Contato
from agenda import Agenda

c1 = Contato("", 0, "")
c1.nome = "João"
c2 = Contato("Maria", 987654321, "maria@email.com")
c3 = Contato("Pedro", 0, "pedro@email.com")
c4 = Contato("Ana", 111111111, "ana@email#com")

agenda = Agenda()
agenda.salvar_contato_agenda(c1)
agenda.salvar_contato_agenda(c2)
agenda.salvar_contato_agenda(c3)
agenda.salvar_contato_agenda(c4)

agenda.pesquisar_todos_contatos()
print("---------------------------------")

contato_pesquisado : Contato | None = \
            agenda.pesquisar_por_numero(
                int(input("Digite o número desejado: "))
            )
if contato_pesquisado == None:
    print("Contato não encontrado!")
else:
    print(contato_pesquisado)
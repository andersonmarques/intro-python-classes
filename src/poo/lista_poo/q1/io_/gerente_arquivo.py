class Gerente_Arquivos:
    # tipos de acao ao trabalhar com arquivos:
    # w: escrever (write)
    # a: adicionar uma linha no final do arquivo (append)
    # r: ler      (read)

    def escrever_arquivo(self, conteudo, acao = 'a'):
        with open('arquivo.txt', acao, encoding='utf-8') as arq:
            arq.write(f"{conteudo}\n")

    def ler_todo_arquivo(self, dir_arquivo: str):
        '''Entrega todo arquivo de uma unica vez'''
        with open(dir_arquivo, 'r', encoding='utf-8') as arq:
            return arq.read() 

    def ler_uma_linha_arquivo(self, dir_arquivo: str):
        '''Entrega uma linha por vez'''
        with open(dir_arquivo, 'r', encoding='utf-8') as arq:
            return arq.readline() 

    def ler_todas_linhas_arquivo(self, dir_arquivo: str):
        '''Entrega uma lista com as linhas do arquivo'''
        with open(dir_arquivo, 'r', encoding='utf-8') as arq:
            return arq.readlines() 
    


gerente = Gerente_Arquivos()

# print(gerente.ler_todo_arquivo(dir_arquivo='arquivo.txt'))
# print(gerente.ler_uma_linha_arquivo('arquivo.txt'))
print(gerente.ler_todas_linhas_arquivo('arquivo.txt'))
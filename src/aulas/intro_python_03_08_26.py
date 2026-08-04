"""Exemplos introdutórios da aula de Python.

O arquivo reúne, em uma sequência didática, exemplos de saída, variáveis,
tipos de dados, operadores, funções e estruturas de repetição.
"""

import math


def demonstrar_saida_e_variaveis() -> None:
    """Apresenta comandos de saída, strings e variáveis."""
    print("Olá, mundo!")  # comando de saída

    # O endereçamento de memória é feito em hexadecimal.
    # Exemplo: 0x7ffdfc3b8c10 = Anderson
    # O nome da variável funciona como um apelido para esse endereço.
    # nome = input("Qual seu nome?")  # comando de entrada

    print('string 123 @#$~]ao aspas "duplas"')

    nome: str = "Anderson"
    idade: int = 32
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")


def demonstrar_tipos_de_dados() -> list[str]:
    """Cria exemplos dos principais tipos de dados básicos do Python."""
    linguagem: str = "Python"
    idade: int = 32
    salario: float = 1000.00
    recebeu_bonus: bool = False
    numero_complexo: complex = 1 + 2j
    lista_alunos: list[str] = ["Anderson", "Maria", "José"]
    tupla_alunos: tuple[str, ...] = ("Anderson", "Maria", "José")
    dicionario_palavras: dict[str, str | list[str]] = {
        "Friend": "amigo",
        "Girls": ["Menina", "Garota", "Moça"],
        "Bear": "Urso",
    }
    conjunto_estados: set[str] = {"SP", "RJ", "MG", "PA"}

    print("\nTipos de dados:")
    print(type(numero_complexo))
    print(f"Linguagem: {linguagem}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario:.2f}")
    print(f"Recebeu bônus: {recebeu_bonus}")
    print(f"Número complexo: {numero_complexo}")
    print(f"Alunos: {lista_alunos}")
    print(f"Tupla de alunos: {tupla_alunos}")
    print(f"Dicionário: {dicionario_palavras}")
    print(f"Estados: {conjunto_estados}")

    return lista_alunos


def demonstrar_operadores() -> None:
    """Apresenta operadores aritméticos, relacionais e lógicos."""
    print("\nOperadores aritméticos:")
    print(f"Adição: {2 + 2}")
    print(f"Subtração: {5 - 3}")
    print(f"Multiplicação: {4 * 3}")
    print(f"Divisão: {10 / 2}")
    print(f"Divisão inteira: {10 // 3}")
    print(f"Resto da divisão: {10 % 3}")
    print(f"Exponenciação: {2 ** 3}")
    print(f"Raiz quadrada: {16 ** 0.5}")
    print(f"Raiz quadrada com math.sqrt(): {math.sqrt(16)}")

    # Operadores de comparação: ==, !=, >, <, >= e <=.
    # Operadores lógicos: and, or e not.


def soma(a: int, b: int) -> int:
    """Retorna a soma de dois valores, aceitando apenas a >= 0."""
    if a < 0:
        raise ValueError("O valor de 'a' não pode ser negativo")
    return a + b


def percorrer_lista(lista: list[str]) -> None:
    """Percorre uma lista usando um laço while."""
    indice = 0
    while indice < len(lista):
        print(lista[indice])
        indice += 1


def demonstrar_repeticao() -> None:
    """Demonstra um laço contínuo com uma opção para encerramento."""
    print("\nRepetição:")
    while True:
        resposta = input("Deseja continuar? (s/n): ").strip().lower()
        if resposta == "n":
            break
        if resposta == "s":
            print("A repetição continua.")
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")


def main() -> None:
    """Executa os exemplos da aula na ordem em que os conceitos aparecem."""
    demonstrar_saida_e_variaveis()
    lista_alunos = demonstrar_tipos_de_dados()
    demonstrar_operadores()

    print(f"\nResultado da soma: {soma(2, 3)}")
    demonstrar_repeticao()

    print("\nAlunos percorridos com while:")
    percorrer_lista(lista_alunos)


if __name__ == "__main__":
    main()

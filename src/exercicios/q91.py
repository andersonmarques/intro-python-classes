maior :int = -1000
menor :int = 1000000000 # valor inicial para o menor
while True:
    valor = int(input("Digite um conj de valores:"))
    if valor < 0:
        print("Valor inválido. Digite um valor + ou 0 para encerrar.")
        continue #aborta essa iteração e volta para o início do while
    if valor == 0:
        break # encerra o while
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
x = -1
cont_impar = 0
for i in range(1, 11):
    x = int(input(f"Digite o {i}º valor:\n"))
    if (x % 2) != 0:
        cont_impar += 1
print(f'Total de impares: {cont_impar}')
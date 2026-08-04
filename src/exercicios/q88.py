# for - sei o limite de rep
x = -1
cont = 0
while x != 0:
    x = int(input('Digite um valor:\n'))
    if 100 <= x <= 200:
        cont += 1
print(f"Total: {cont}")
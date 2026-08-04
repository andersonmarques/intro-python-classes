#entrada
v1,v2,v3,v4=map(float, input("Digite 4 valores:").split())
#processamento
somatorio = v1 + v2 + v3 + v4
media = somatorio / 4
p1 = (v1 * 100) / somatorio
p2 = (v2 * 100) / somatorio
p3 = (v3 * 100) / somatorio
p4 = (v4 * 100) / somatorio
#saida
print(f"O somatório dos valores é: {somatorio}")# f-string

print(f"A média dos valores é: {media}")# f-string

print(f"Porcentagens: {p1:.2f}%, {p2:.2f}%, {p3:.2f}%, {p4:.2f}%")
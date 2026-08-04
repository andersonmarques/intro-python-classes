from math import sqrt
a, b, c = map(float,input("a, b e c:\n").split())# 1.0 2.0 3.0
delta = b ** 2 - 4 * a * c
# condição -> se
if delta < 0:
    print("Opa! o Delta é negativo.")
elif delta == 0:
    raiz_1 = (-b + sqrt(delta)) / (2 * a)
    raiz_2 = raiz_1
else:
    raiz_1 = (-b + sqrt(delta)) / (2 * a)
    raiz_2 = (-b - sqrt(delta)) / (2 * a)
print(f"Delta: {delta}\nRaiz 1: {raiz_1}\nRaiz 2: {raiz_2}")
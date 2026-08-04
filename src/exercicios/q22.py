v1, q1 = map(float,input('valor 1 e a quant 1:\n').split())
v2, q2 = map(float,input('valor 2 e a quant 2:\n').split())
v3, q3 = map(float,input('valor 3 e a quant 3:\n').split())

total = q1 * v1 + q2 * v2 + q3 * v3

print(f'Total: {total:.2f}')

conta_bancaria = input("Qual sua conta?")
saldo = float(input("Qual seu saldo?"))
op = input("(D)epósito | (S)aque:\n").upper()
valor_operacao = float(input('Digite o valor:\n'))

if op == 'D':
    saldo += valor_operacao # saldo = saldo + valor_operacao
else:
    if saldo == 0 or valor_operacao > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor_operacao

print(f'Saldo: {saldo}')

from cliente import Cliente
from pedido import Pedido
from tipo_pagamento import Tipo_Pagamento
from item import Item
from produto import Produto


arroz = Produto(nome = "Arroz", preco = 5.99, quant_estoque = 100)
feijao = Produto(nome = "Feijão", preco = 7.49, quant_estoque = 80)
macarrao = Produto(nome = "Macarrão", preco = 2.29, quant_estoque = 120)

cliente1 = Cliente("Edimar", "123.456.789-00")
cliente2 = Cliente("Emerson")
cliente2.cpf = "987.654.321-00"
cliente3 = Cliente("David")
print(cliente1)
print(cliente2)
print(cliente3)

pedido_cliente3 = Pedido(Tipo_Pagamento.DEBITO)

pedido_cliente3.adicionar_item(Item(arroz, 2))
arroz.quant_estoque -= 2 # arroz.quant_estoque = arroz.quant_estoque - 2
print(f"Quant. em estoque de {arroz.nome}: {arroz.quant_estoque}")

pedido_cliente3.adicionar_item(Item(feijao, 1))
feijao.quant_estoque -= 1
print(f"Quant. em estoque de {feijao.nome}: {feijao.quant_estoque}")

pedido_cliente3.adicionar_item(Item(macarrao, 3))
macarrao.quant_estoque -= 3
print(f"Quant. em estoque de {macarrao.nome}: {macarrao.quant_estoque}")

print(pedido_cliente3.tipo_pagamento)
print(f"Total do Cliente:{cliente3.nome}: \
      R${pedido_cliente3.total():.2f}")



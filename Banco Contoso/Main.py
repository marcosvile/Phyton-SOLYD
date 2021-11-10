#  Software de gerenciamento bancário

# Exercicio Aula 09
# Crie um software de gerenciamento bancario
# esse software devera ser capaz de criar clientes e contas
# cada cliente possui:
# nome 
# cpf 
# idade

# cada conta possui:
# cliente - cliente dono da conta
# saldo
# limite
# sacar
# depositar 
# e consultar saldo 

from cliente import Cliente
from conta import Conta

cliente1 = Cliente('marcos', '123.123.123.12', 27)

print(cliente1)

conta_marcos = Conta(cliente1, 10.50, 1000)

print(conta_marcos.cliente.nome, conta_marcos.saldo, conta_marcos.consulta)

conta_marcos.depositar(1045.55)

print(conta_marcos.saldo)

conta_marcos.sacar(500)

print(conta_marcos.saldo)

conta_marcos.sacar(600)

print(conta_marcos.saldo)
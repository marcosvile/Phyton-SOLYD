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

from class cliente import Cliente
from conta import Conta

cliente1 = cliente('marcos', '123.123.123.12', 10.50)

print(cliente1)
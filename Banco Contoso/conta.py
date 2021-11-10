class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite #criacao do limite, para ter a opçao de limite negativo

    def depositar (self, quantidade): #criação do metodo depositar
        if quantidade > 0:              # verificaçao se a quantia a depositar é maior que 0
            self.saldo += quantidade    
        else:
            print("erro no deposito")

    def consulta (self):               #criaçao do metodo de consulta do saldo
        return self.saldo               #return no self.saldo para nao precisar printar só o saldo

    def sacar (self, quantidade):       # criaçao do metodo sacar
        if self.saldo - quantidade < self.limite:
            print("saldo insuficiente: ")
        else:
            self.saldo -= quantidade

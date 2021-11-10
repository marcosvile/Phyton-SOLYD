class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar (self, quantidade):
        if quantidade > 0:
            self.saldo += quantidade
        else:
            print("erro no deposito")

    def consulta (self):
        return self.saldo
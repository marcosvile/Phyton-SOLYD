class Cliente:

    def __init__(self, nome, cpf, idade): # definiu o cliente
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome, + "\nCPF: " + self.cpf, + "\nIdade: " + self.idade 
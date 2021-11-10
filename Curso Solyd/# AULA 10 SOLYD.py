# AULA 10 SOLYD
arquivo=open('teste.txt', 'w')

type=(print(arquivo))

print(arquivo)

arquivo.write("teste de ediçao no arquivo ")

for i in range(0, 100):
    arquivo.write("1234 " + str(i) + "\n" )

arquivo = open('teste.txt', 'w')

print(arquivo.read() )
# AULA 11 SOLYD

# TRY E EXCEPT

import time

def abrearquivo():
    try:
        arquivo = open( 'teste.txt')
        return True
    except Exception as erro:
        print ("houve um erro na abertura do arquivo: ", erro)
        return False

while not abrearquivo():
    print("tentando abrir o arquivo")
    time.sleep(5)
    
print('conseguiu abrir o arquivo')
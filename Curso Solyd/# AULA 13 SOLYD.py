# AULA 13 SOLYD

# Consumo de API E Json - API da omdb nao esta funcionando mesmo com key

import requests
import json

def requisicao(reqtitle):

    try:


        req = requests.get("http://www.omdbapi.com/?apikey=d00f3f58&=" + reqtitle)
        dic = json.loads(req.text)
        return dic

    except:
        print( "Erro na conexão ")    
        return None

def printar(filme):
    print('titulo: ', filme["Title"])

sair = False
while not sair:
    op = input("escreva um nome de uma iflme ou SAIR para fechar: ")
    
    if op == "sair":
        sair = True
        print("saindo")
        
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('nao encontrado')
        else:
            printar(filme)
            
            
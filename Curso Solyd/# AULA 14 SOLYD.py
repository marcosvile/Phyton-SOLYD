# AULA 14 SOLYD ---=-

# Expressões regulares

# padrao de email - email@dominio.com.br
# Expressões regulares também chamados de regex

import re
import requests sss

teste_search = 'o gato é bonito, a gata, o gatao.com os gatinhos, rh@exemplo.com, dp@exemplo.com'

padrao = re.search(r'tempest', teste_search) #r -> transforma o parametro de busra em RAW STRING
                                             #\w -> busca caracteres do tipo texto, numeros e caracters
                                             # sem considerar espaços em brancos, considerando a sequencia \w 

if padrao:
    print(padrao.group())
else:
    print("padrao nao encontrado")

padrao = re.findall(r'gat\w+\.', teste_search)

if padrao:
    print(padrao)
else:
    print("padrao nao encontrado")
    
padrao = re.findall(r'[gat]+\w', teste_search)

if padrao:
    print(padrao)
else:
    print("padrao nao encontrado")
    

requisicao = requests.get("https://exemplo.com.br/contato")

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print("padrao nao encontrado")

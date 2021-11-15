# AULA 14 SOLYD 

# Expressões regulares

# padrao de email - email@tempest.com.br
# Expressões regulares também chamados de regex

import re

teste_search = 'o gato é bonito'

padrao = re.search(r'tempest', teste_search) #r -> transforma o parametro de busra em RAW STRING

if padrao:
    print(padrao.group())
else:
    print("padrao nao encontrado")


# Exercicio - programa que busque a cotação do dolar e clima em tempo real

import re
import requests

requisicao = requests.get('https://br.investing.com')

padrao = re.findall(r'dolar', requisicao.text)

if padrao:
    print(padrao)
else:
    print("padrao nao encontrado")

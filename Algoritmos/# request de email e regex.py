# request de email e regex

import re
import requests

requisicao = requests.get('https://lacoxinha.com.br/contato')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao[requisicao.text])
else:
    print("padrao nao encontrado")
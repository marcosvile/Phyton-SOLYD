# Exercicio - programa que busque a cotação do dolar e clima em tempo real

# https://economia.awesomeapi.com.br/last/USD-BRL

import re
import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

print(requisicao.text)

cotacao = json.loads(requisicao.text)

print(cotacao['USDBRL'])
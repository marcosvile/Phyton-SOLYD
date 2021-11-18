# Exercicio - programa que busque a cotação do dolar e clima em tempo real

# https://economia.awesomeapi.com.br/last/USD-BRL

import re
import requests
import json

requisicao = requests.get('https://www.mercadobitcoin.net/api/BTC/trades')

print(requisicao.text)

cotacao = json.loads(requisicao.text)

print(cotacao['price'])
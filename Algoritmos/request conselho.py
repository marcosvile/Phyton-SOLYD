# Request conselho grátis
# este algoritmo busca uma frase de efeito aleatorio de uma API gratis da web

import requests
import json


requisicao = requests.get('https://api.adviceslip.com/advice');

conselho = json.loads (requisicao.text)

print(conselho['slip']['advice'])
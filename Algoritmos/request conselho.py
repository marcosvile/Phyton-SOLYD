# Request conselho grátis

import requests
import json


requisicao = requests.get('https://api.adviceslip.com/advice')

conselho = json.loads (requisicao.text)

print("conselho grátis: ", conselho['slip'])
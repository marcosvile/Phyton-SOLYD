# AULA 12 SOLYD

# requisições web

import sys
import urllib
import requests

cabecalho = {"User-agent": "Windows 18",
             'Referer': "https://google.com",
             'cf-ipcountry': "BK"}

meus_cookies = {"Ultima-visita": '10-10-1994'}
texto = None

try:
    requisicao = requests.post('https://putsreq.com/WxMoXb7ziLSCCNcARF0s', headers=cabecalho, cookies=meus_cookies)                
    texto = requisicao.text
    
except Exception as e:
    print("requisicao deu erro: ", e)

print(texto)



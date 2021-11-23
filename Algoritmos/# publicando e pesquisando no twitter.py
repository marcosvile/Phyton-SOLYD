# publicando e pesquisando no twitter

# #Requisição REST retorna JSON
# Oauth, autenticação
# O método abaixo serve para qualquer API que usa o Oauth

# import oauth.oauth 
# import oauth2 as oauth
import json
import requests
import oauth2 #as oauth

consumerkey = 'euVS6EpyjhaGomigXJhY5RquT'
keysecret = 'egknpux5Q0ilr0aUq7YoVOQogrJWVc6xYD727Fv0uhjOXZI7m6'
consumertoken = 'AAAAAAAAAAAAAAAAAAAAAM5TWAEAAAAAd7qiFpneqVkzoHm4UPHcZGREAvw%3DpVZn8nSMxnM1fOSFW2yoAO26TjXlh1QuBjR2riHeja358Bah7C'

consumer = oauth2.Consumer (consumerkey, keysecret)

token = oauth2.token (consumertoken, keysecret)

cliente = oauth2.cliente (consumer, token)

requisicao = cliente.request ('https://api.twitter.com/1.1/search/tweets.json?q=brasil')

print(requisicao)

# pretty print
#import pprint

# Transforma a Hash em porcentagem
#import urllib.parse
# Consumer
#consumer_key = ''
#consumer_secret = ''

# Token
#access_token = ''
#access_token_secret = ''

# Perceba como as coisas se encaixam feito peças de Lego:
#consumer = oauth2.Consumer(consumer_key, consumer_secret)
#token = oauth2.Token(access_token, access_token_secret)
#cliente = oauth2.Client(consumer, token)

#pesquisa = input('O que você quer achar no Twitter?: ')
#pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')
# Pegar no site, search API
# É como no Requests
# A primeira parte da requisição vem como Tupla
# A segunda parte vem como byte
# No Python 3 há diferença entre Byte e String e por isso precisamos decodificar
#requisicao = cliente.request("https://api.twitter.com/1.1/search/tweets.json?q="+pesquisa_codificada)
# Está transformado em Lista, dict
#requisicao_decodificar = requisicao[1].decode()
#requisicao_objeto = json.loads(requisicao_decodificar)
#posts = requisicao_objeto['statuses']

# pprint imprime as coisas de forma bonitas

#for post in posts:
 #   print(post['user']['screen_name'])
  #  print(post['text'])
   # print()

#twittar = input('O que você está pensando?: ')
#twittar_codificada = urllib.parse.quote(twittar, safe='')
# O padrão aqui está Get, precisa ser POST
#requisicao_twittar = cliente.request("https://api.twitter.com/1.1/statuses/update.json?status="+twittar, method='POST')
#twittar_decodificar = requisicao_twittar[1].decode()
#twittar_objeto = json.loads(twittar_decodificar)

#print(twittar_objeto)
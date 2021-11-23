

import json
import requests
import oauth2

consumerkey = 'euVS6EpyjhaGomigXJhY5RquT'
keysecret = 'egknpux5Q0ilr0aUq7YoVOQogrJWVc6xYD727Fv0uhjOXZI7m6'
consumertoken = 'AAAAAAAAAAAAAAAAAAAAAM5TWAEAAAAAd7qiFpneqVkzoHm4UPHcZGREAvw%3DpVZn8nSMxnM1fOSFW2yoAO26TjXlh1QuBjR2riHeja358Bah7C'

consumer = oauth2.Consumer (consumerkey, keysecret)

token = oauth2.Token (consumertoken, keysecret)

cliente = oauth2.Client (consumer, token)

requisicao = cliente.request ('https://api.twitter.com/1.1/search/tweets.json?q=brasil')

print(requisicao)
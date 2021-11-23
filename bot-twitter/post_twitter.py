# funcao que realiza o post no twitter
# o mesmo pega os arquivos de configuração que servem para autenticar no perfil

import tweepy
import settings

from funcao_conselho import get_random_conselho
 
CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']

ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(get_random_conselho())
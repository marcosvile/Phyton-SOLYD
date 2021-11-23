#consumer keys:
# api key gPiZzk9nRg0YZABbk0lExWTlh
# api secret key 6yKSWYoJFDnmI2PqzvZEfKwFTojp7763hdbcYilxr7XQ7ZaCTY

#authentication tokens:
# bearer token AAAAAAAAAAAAAAAAAAAAAEZZWAEAAAAAMGoEHCMbZrVoA6PjY31qyP9tmXs%3Dq3gqI7mgXJPNbcj1xIeN1UNQH9g7mM6L1iv83gaHwIxNTjXDSd

# access token 1457323725305614337-C8EF4XYtxnu3QcZPsDUMicJrlTq7ve
# access token secret yiAEDNzl1AXh0uKKVip9rCM2wVgnVtr7bcvBYbYyHukFR

import tweepy, time, sys
import settings
from issues import get_random_conselho
 
CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']

ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(get_random_conselho())
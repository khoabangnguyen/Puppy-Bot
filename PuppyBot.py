import tweepy as tp
import time
import os

consumer_key = 'TZH35INeG6Og3VD2O7A5p0OiY'
consumer_secret = 'VZs3lWSvJu2Zz6LBor8aMRpot4ptQVuUqvmKQ8HmSHisXgaO0j'
token = '1236846419597840387-LfcX49CbZekwahOog7E0RsJ9exSBwK'
token_secret = 'NIexXfDd7GfADqUPIJ0xSw6S1MHSnnFhnWzPuyQUpKs9f'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tp.API(auth)

os.chdir('Puppies')
for pic in os.listdir('.'):
    api.update_with_media(pic)
    time.sleep(3)

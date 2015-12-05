import twitter
import secrets

api = twitter.Api(consumer_key=secrets.consumer_key, #'consumer_key',
                  consumer_secret=secrets.consumer_secret, #consumer_secret',
                  access_token_key=secrets.access_token, #'access_token',
                  access_token_secret=secrets.access_token_secret) #'access_token_secret')

import tweepy, sys

# Create variables for each key, secret, token
consumer_key = 'vVCZ3YAYempvjdWMTh2nQAqyl'
consumer_secret = 'XPhTonpHBxKSXNdf1SSJgqYWmZdEHKbGTjGG5WlyZZjCTnovsZ'
access_token = '2180284776-wlDi1ZYlpdZw7RpenDdL7BmS3rnTgbR8q1OHw7N'
access_token_secret = 'Q0Mo7gosc6xzDFQov0YxL3nJ2OF0BOdhq4gaYE2PQ3ONP'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = sys.argv[1]
api.update_status(status=str(tweet))

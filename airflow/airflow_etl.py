
import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

# bearer = AAAAAAAAAAAAAAAAAAAAAGhlmAEAAAAAnFYjnWSlEBF%2FiqThlHKBtJgI0AM%3DiVBSxfbAIkTY1Lh76BhmgcWVml7yWx8iaFG61mgvgCsftHB4Ka


api_key = "rEYScGUNFEpzXqqhVC11tKTMc"
api_secret = "Q14csXz4LpGdLCjKRlmYYbC5jkOWt4WKCx6VLswcbOXgC4fJ6M"
access_key = "1509634098058383367-G8KJtbROhGbUJ9bKNhpRMGvYzVVy44"
access_secret = "gT4bxzx2wmqIRGi92GPGOE0F4md5rLd0Pi93HBRY86ORu"

#twitter authenctication
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_key,access_secret)


#creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                          #200 is the maximum allowed count
                          count = 200,
                          include_rts = False,#extract the tweet which elon musk saw
                          #Necessary to keep full_text
                          #otherwise only the first 140 words are extracted
                          tweet_mode = 'extended'
                          )

print(tweets)
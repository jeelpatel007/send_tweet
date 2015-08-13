# Tweepy is used to access the Twitter API
import tweepy

# **get_api** takes the auth values and pushes it to twitter API using Tweepy
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

# **main** gets the data to be used in *get_api* 
def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "VALUE_HERE",
    "consumer_secret"     : "VALUE_HERE",
    "access_token"        : "VALUE_HERE",
    "access_token_secret" : "VALUE_HERE" 
    }

  api = get_api(cfg)
  tweet = raw_input("Enter your Tweet: \t")
  status = api.update_status(status=tweet)

if __name__ == "__main__":
  main()

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name) # print your name
print(user.screen_name)
print(user.followers_count)

search = "Aiden Tran"
numberOFTweets = 2

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

# Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == "Usernamehere":
        follower.follow()


# Be a narcisist amd love your own tweets, or retweet anything with a keyword!
for tweet in tweet.Cursor(api.search, search).items(numberOFTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


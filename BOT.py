import tweepy
import time

auth = tweepy.OAuthHandler('1qfBF6V8rz7b1ZvzQPGBibGp9','qG29bZLSL9jHQoxZpUuq6FemalrP7FqSoIuoTp1BhiYuk6P6Ia')
auth.set_access_token('732084240725217280-4r4O40IJaEOVKawlHAntduzRusgAhv1','R2CAGu2faQYTTnfzNVqVqjb6p62jb6CX0ffd18CrNv6cA')

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

search='@BJP4India'#you can replace this with hashtag also OR we can create a array to like tweet from multiple account
for tweet in tweepy.Cursor(api.search,search).items(100):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

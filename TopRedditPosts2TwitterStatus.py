import praw
import datetime
import tweepy

#Check apps.twitter.com for consumer key, consumer secret, 
#access token, and acess token secret
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
twitterAuth = tweepy.OAuthHandler(consumer_key, consumer_secret)
twitterAuth.set_access_token(access_token, access_token_secret)
api = tweepy.API(twitterAuth)

#Our unique reddit agent
agent='Your unique agentx name '+ str(datetime.datetime.now()) #and of course adding time to make it more unique
r = praw.Reddit(user_agent=agent)

posts = r.get_subreddit('netsec').get_top_from_day(limit=1)
for post in posts:
    if len(post.title) + len(post.short_link) < 139:
        status = (post.title + " " + post.short_link)
        print(status)
        api.update_status(status)





import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from colorama import Fore,Back,Style,init
import datetime
ch=0
hash=0
class TwitterClient(object):
    p_tweets=0
    n_tweets=0
    neu_tweets=0
    total_tweets=0

    #initialize the object with user credentials
    def __init__(self):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_key = 'your_access_key'
        access_secret = 'your_access_secret'
        init(convert=True)
         
        try :
            self.auth = OAuthHandler(consumer_key,consumer_secret)
            self.auth.set_access_token(access_key,access_secret)
            self.api = tweepy.API(self.auth)
        except :
            print("Authentication failed\n")

    #clean the tweet by removing unwanted symbols
    def clean_tweet(self, tweet): 
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 


    #fetch the tweets and store them
    def fetch_tweets(self,query,c):
	
        self.total_tweets = int(c)
        tweets = []
        date = datetime.datetime.now()
        date=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
        try:

          fetched_tweets = tweepy.Cursor(self.api.search,q=query + " -filter:retweets",lang="en",since=date,tweet_mode='extended').items(int(c))
          for tweet in fetched_tweets :
            parsed_tweets = {} 
            parsed_tweets['text']=tweet.full_text
            parsed_tweets['sent']=self.AnalyseTweet(tweet.full_text)
            print(Back.WHITE)
            print(Fore.BLACK  + parsed_tweets['text'])
            if parsed_tweets['sent'] == 'Positive':
                print(Fore.GREEN + " " + parsed_tweets['sent'] + " ")
            elif parsed_tweets['sent'] == 'Neutral' :
                print(Fore.BLACK + " " + parsed_tweets['sent'] + " ")
            else : 
                print(Fore.RED + " " + parsed_tweets['sent'] + " " )
            print(Style.RESET_ALL + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        except tweepy.TweepError as e:
          print(str(e))

    def AnalyseTweet(self,tweet):
        res = TextBlob(self.clean_tweet(tweet))
        if res.sentiment.polarity > 0:
            self.p_tweets = self.p_tweets + 1
            return 'Positive'
        if res.sentiment.polarity == 0:
            self.neu_tweets = self.neu_tweets + 1
            return 'Neutral'
        if res.sentiment.polarity < 0:
            self.n_tweets = self.n_tweets + 1
            return 'Negative'


tc = TwitterClient()
print("Enter hashtag : #",end="")
hash = input()
print("Enter number of tweets : ",end="")
count=input()
tc.fetch_tweets("#"+hash,count)
print(Style.RESET_ALL)
print("Positive Tweets : " + str((tc.p_tweets/tc.total_tweets)*100) + "%")
print("Neutral Tweets : " + str((tc.neu_tweets/tc.total_tweets)*100) + "%")
print("Negative Tweets : " + str((tc.n_tweets/tc.total_tweets)*100) + "%")

	

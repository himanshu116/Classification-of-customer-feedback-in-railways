import tweepy
import re
consumer_key="b2uDWq9LTwOGWln6l5FvTpeT9"
consumer_secret="Y8ua0tnUE3qik3J9FmFcqYMEaQzdvAeGccNYmsrDuFMX29RkT5"
access_token="723196595722809345-SncjK4V2KgWljDifS1j526D75heDUdW"
access_token_secret="GKf5QwWO30m5PsvuLqWbnEfOZjV7JVWghsfY0Md1aMocv"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
#         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
#         # Access to user's access key and access secret
#         auth.set_access_token(access_key, access_secret)
 
#         # Calling api
#         api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets =  api.search(q=username, count=2, lang='en')
        # Empty Array
        tmp=[] 
        
        # create array of tweet information: username, 
        # tweet id, date/time, text
        '''
        tweets_for_csv = [tweet for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
            # Appending tweets to the empty array tmp
            k = re.sub(r'@\w+',"", j.text)
            print(k)
            tmp.append(k) 

        return tmp
        '''
        cursor= tweepy.Cursor(api.search,q=username, tweet_mode='extended',lang="en").items(5)

        for tweet in cursor:
            k = tweet.full_text
            #k = re.sub(r'@\w+',"", k)
            tmp.append(k)
        
        return tmp
        # Printing the tweets
        

'''
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("railminindia")
'''
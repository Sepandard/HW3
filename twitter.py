from socialMedia import SocialMediaClass
from service.twitterTweetList import tweetList

class TwitterClass(SocialMediaClass):
    
    def createNewTweet(self,body):
        charNumber =  body.count('') - 1 
        print('Trying add tweet: ',body[:25])
        if charNumber < 280:
            tweetList.append(body)
            print('Notification: [Tweet Successfully Added]')
        else: 
            print("ERROR: [Tweet is Too Long]")

    def getTweets(self):
        print('---------------------')
        print('TWEETS LIST')
        print('')
        for index, tweet in enumerate(tweetList):
            print(str(index+1) + '. ' + tweet)
            print('---------------------')    
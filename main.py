from instagram import InstagramClass
from twitter import TwitterClass


newInstagram = InstagramClass ('---- Instagram ----') 

print(newInstagram.getName())
newInstagram.publishNewPost ('hello') 
newInstagram.publishNewPost ('this is my first post') 
newInstagram.getPost()




newTwitter = TwitterClass ('\n ---- Twitter ----') 

print(newTwitter.getName())
newTwitter.createNewTweet ('hello') 
newTwitter.createNewTweet ('this is my first Tweet') 
newTwitter.getTweets()
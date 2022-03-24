from socialMedia import SocialMediaClass
from service.instagramPostList import PostList

class InstagramClass(SocialMediaClass):
    
    def publishNewPost(self,body):
        charNumber =  body.count('') - 1 
        print('Trying add post: ',body[:25])
        if charNumber < 2200:
            PostList.append(body)
            print('Notification: [Post Successfully Added]')
        else: 
            print("ERROR: [Caption Too Long]")

    def getPosts(self):
        print('---------------------')
        print('POSTS LIST \n')
        
        for index, post in enumerate(PostList):
            print(str(index+1) + '. ' + post)
            print('---------------------')    

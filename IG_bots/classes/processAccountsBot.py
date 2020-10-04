import sys
sys.path.insert(1, '../')
from selenium.webdriver.common.keys import Keys
import random
from random import randint

from functions import fetchLists, wait, chanceOccured, cleanNumber, updateLists
from bot import Bot

class ProcessAccountsBot(Bot):
    def __init__(self, account: str = None):
        super().__init__()        
        if (account is not None):            
            self.initialUsers, self.notFollowed, self.followed, self.privateRequested = fetchLists(account)
            self.initialAccount = account                        
        
   
    def alreadyStored(self, user: str):
        if (user in self.notFollowed or user in self.followed or user in self.privateRequested):
            return True
        else:
            return False
    
    
    #gotta wait til ban to find out the english word haha
    def isBan(self):
      try:
          if (self.browser.find_element_by_tag_name('h2').text == 'Fehler'):
              print('BAN')
              return True
          return False
      except:
          return False    
  
    
    def isHashtag(self):    
        try:
            if (self.browser.find_element_by_class_name('_7UhW9.fKFbl.yUEEX.KV-D4.uL8Hv').text[0]=='#'):
                print('HASHTAG')
                return True
            return False
        except:
            return False    
       
        
    def isLocation(self):
        try:
            self.browser.find_element_by_class_name('leaflet-tile.leaflet-tile-loaded')
            print('LOCATION')
            return True
        except:            
            return False    


    def isPrivate(self):
        try:
            self.browser.find_element_by_class_name('rkEop') # privat            
            return True
        except:
            return False    
        
    def isUnexisting(self):
        try:
            if (self.browser.find_element_by_class_name('VnYfv').text == "Sorry, this page isn't available."):
                return True
            return False
        except:
            return False
        


    def getCurrentUserData(self, user: str):
        posts =  int(cleanNumber(self.browser.find_elements_by_class_name('g47SY')[0].text))
        isFollowedBy = int(cleanNumber(self.browser.find_elements_by_class_name('g47SY')[1].text))
        isFollowing = int(cleanNumber(self.browser.find_elements_by_class_name('g47SY')[2].text))
        return user, posts, isFollowedBy, isFollowing


    def isCandidateForFollow(self, userStats: (int, int, int)):
        #0.85 represents follower -> following - threshold to which a user is a candidate        
        if (userStats[1] >= 12 and userStats[2] in range(300, 5000) and (userStats[2] <= 0.85 * userStats[3])):
            return True
        else:
            return False
        
        
    def isCandidateForProcessing(self, userStats: (int, int, int)):            
        if (not self.isPrivate() and userStats[1] >= 25 and userStats[2] > 1500):
            return True
        else:
            return False

    
    def processAccount(self, user, commentChance):        
        randomIndeces = []
        while (len(randomIndeces) < 3):            
            y = randint(0,2)            
            if (y not in randomIndeces):
                randomIndeces.append(y)                 
        commentControl = random.choice(randomIndeces)    
        for index in randomIndeces:
            self.browser.find_elements_by_class_name('eLAPa')[index].click()
            wait(8,10)
            self.likePost()
            wait(6,8)
            if (commentControl == index):                
                if(chanceOccured(commentChance)):
                    try:
                        self.insertComment(user)                        
                    except Exception as e:
                        print('Blocked Commenting')
                        print(e)                                        
            self.actions.send_keys(Keys.ESCAPE).perform()
            wait(5,8)
            self.actions.reset_actions()        
        self.actions.key_down(Keys.SHIFT) # Before following, go to the top of the page by simulating shift and space
        self.actions.send_keys(' ')
        for i in range(2):                    
            self.actions.perform()            
            wait(3,5)  
        self.actions.reset_actions()
        
        
    
    def processAccountList(self):        
        notFollowedUsers = []
        followedUsers = []
        privateUsers = []
        # gets increased by 2 for each processing and by 1 for each following
        banControl = 0
        try:
            for user in self.initialUsers:
                if (self.alreadyStored(user)):
                    print('continuamous: User already stored')
                    continue    
                print(banControl)
                # threshold can be met by (18 + 2; 19 + 1; 19 + 2); Bot NEEDS to take a 10-15 min break
                if (banControl not in (0,1) and (banControl % 20 in (0,1))):
                    print('WAITING!')
                    banControl = 0
                    wait(600,900)
                
                if (not self.searchUser(user)):
                    print('continuamous: Something went wrong in the search')
                    continue
                if (self.isUnexisting() or self.isBan() or self.isHashtag() or self.isLocation()):
                    print('continuamous: not a user; BAN; Hashtag; Location')
                    continue                        
                userData = self.getCurrentUserData(user)
                print(userData)
                if (self.isCandidateForFollow(userData)):                
                    if (self.isPrivate()):
                        self.tryFollow()
                        print('private requested')
                        privateUsers.append(userData)                           
                        banControl = banControl + 1
                    else:
                        self.processAccount(user, 33)
                        self.tryFollow()
                        print('public followed')
                        followedUsers.append(userData) 
                        banControl = banControl + 2
                else:
                    if (self.isCandidateForProcessing(userData)):                         
                        self.processAccount(user, 88)
                        print('just processed, not followed')
                        notFollowedUsers.append(userData)
                        banControl = banControl + 2
                        wait(5,10)
                    else:
                        print('not followed')
                        notFollowedUsers.append(userData)
                        wait(5,10)
                        continue                
        except Exception as e:
            print(e)
            
        updateLists(self.initialAccount, notFollowedUsers, followedUsers, privateUsers)
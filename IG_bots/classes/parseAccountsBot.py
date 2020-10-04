import sys
sys.path.insert(1, '../')
from bot import Bot
import time
from random import randint
import os

from functions import wait
import constants as c

class ParseAccountsBot(Bot):        
    def __init__(self):       
        super().__init__()        
        
           
    def parseThroughAccounts(self):  
        print(self.accs)              
        for acc in self.accs:
            if os.path.isdir(c.ROOT_URL + 'accounts/' + acc) :
                continue
            users = set()                   
            self.searchUser(acc)
            self.browser.find_elements_by_class_name('-nal3')[1].click()                        
            wait(2,5)
            self.browser.find_element_by_class_name('PZuss').click() # Click into div to enable Spacebar scrolling; IG blocks instantly; click div again to enable Spacebar            
            wait(5,8)
            self.actions.send_keys(' ').perform()    
            self.actions.reset_actions()
            wait(2,5)
            self.browser.find_element_by_class_name('PZuss').click() # div element - scrolling area            
            t_end = time.time() + randint(1200000, 1500000)/10000 #scrolling simulation in seconds 2 - 2.5 minutes
            while time.time() < t_end:                
                if(randint(1,8) == 1):
                    wait(5,10)
                wait(0.3,0.8)
                self.actions.send_keys(' ').perform()                
            self.actions.reset_actions()                                    
            for user in self.browser.find_elements_by_class_name("FPmhX.notranslate._0imsa"):
                users.add(user.text)                        
            self.browser.get("https://www.instagram.com/")            
            if (not os.path.isdir(c.ROOT_URL + 'accounts/' + acc)) :                
                os.mkdir(c.ROOT_URL + 'accounts/' + acc)                        
            with open(c.ROOT_URL + 'accounts/' + acc + '/' + acc + '_followers.csv', 'w') as file:
                for user in users:
                    file.write(user)
                    file.write('\n')
            with open(c.ROOT_URL + 'accounts/' + acc + '/' + acc + '_followed.csv', 'w') as file:
                print('followed file created')
            with open(c.ROOT_URL + 'accounts/' + acc + '/' + acc + '_not-followed.csv', 'w') as file:
                print('not followed file created')
            with open(c.ROOT_URL + 'accounts/' + acc + '/' + acc + '_private-requested.csv', 'w') as file:
                print('private requested file created')                    
            wait(10,20)                
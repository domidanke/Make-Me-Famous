import sys
sys.path.insert(1, '../')

from functions import fetchLists, wait
from bot import Bot

class ProcessMainPageBot(Bot):
    def __init__(self, account: str = None):
        super().__init__()        
        if (account is not None):            
            self.initialUsers, self.notFollowed, self.followed, self.privateRequested = fetchLists(account)
            self.initialAccount = account   
            
    def watchStories(self):
        try:
            self.browser.find_elements_by_class_name('OE3OK')[0].click()
            print("watching stories")
            wait(60,90)
            self.browser.find_elements_by_class_name('-jHC6')[0].click()
            print("finished watching stories")
        except Exception as e:
            print(e)
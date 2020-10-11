import sys
sys.path.insert(1, '../')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from random import randint

from functions import config, wait

class Bot:
        
    def __init__(self):
        self.creds, self.accs, self.comments = config()      
        self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        #TODO make own ActionChains Manager Class        
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher") 
        wait(2,5)
        self.login()
        self.actions = ActionChains(self.browser)


    def login(self):                    
        self.insert(self.browser.find_element_by_name("username"), self.creds[0])
        wait(2,5)
        
        pw = self.browser.find_element_by_name("password")
        pw.click()    
        self.insert(pw, self.creds[1])
        wait(2,5)
            
        pw.send_keys(Keys.ENTER)    
        self.browser.maximize_window()
        wait(5,8)
        
        # no Save Login Info
        self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
        wait(5,8)
        
        # no notification push
        self.browser.find_element_by_class_name('aOOlW.HoLwm ').click()
        wait(8,10)


    def insert(self, textField, _input):
        for char in _input:
            wait(0.15,0.35)
            textField.send_keys(char)  
    
    
    def searchUser(self, user):        
        search = self.browser.find_element_by_class_name("XTCLo.x3qfX")
        wait(2,5)
        self.insert(search, user)
        wait(10,12)
        try:
            # sometimes the exact user literal does not find the wanted user
            if (self.browser.find_element_by_class_name("Ap253").text != user):
                self.browser.get('https://www.instagram.com/' + user)
                wait(7,12)
                return True
            self.browser.find_element_by_class_name("Ap253").click()
            wait(10,14)
            return True
        except:
            wait(5,8)
            self.browser.find_element_by_class_name("aIYm8.coreSpriteSearchClear").click()
            wait(10,15)
            return False
                                        

    def likePost(self):
        for post in self.browser.find_element_by_class_name('fr66n').find_elements_by_css_selector("*"):
            if(post.get_attribute("class") == '_8-yf5 '):
                if(post.get_attribute("fill") == '#ed4956'):                    
                    break
                else:
                    self.browser.find_element_by_class_name('fr66n').click() # like
                    break     
        wait(4,8)
                
                
    def insertComment(self, user):        
        comment = random.choice(self.comments) + ' '        
        if (randint(0,2)==0):
            comment = comment + '@' + user + ' '            
        commentField = self.browser.find_element_by_class_name('Ypffh')
        commentField.click()    
        commentField = self.browser.find_element_by_class_name('Ypffh')        
        for char in comment:                              
            wait(0.2, 0.6)                
            commentField.send_keys(char)               
        wait(5,8)                                   
        self.actions.send_keys(Keys.ENTER).perform()                        
        wait(5,8)
        self.actions.send_keys(Keys.ESCAPE).perform()   
        wait(5,8)
        self.actions.reset_actions()         
    
    
    def tryFollow(self):
        wait(3,5)
        for button in self.browser.find_elements_by_tag_name("button"):
            if (type(button.text) is not str):
                print('not string')
                continue
            if (button.text == 'Requested' or button.text == 'Following'):
                print('already following')
                break
            if (button.text == 'Follow' or button.text == 'Follow Back'):
                button.click()
                break    
        wait(5,8)

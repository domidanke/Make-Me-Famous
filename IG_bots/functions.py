from random import randint
import time
import csv
import os

import constants as c


# Use local config files to protect data publicly
def config():
    creds = []
    accs = []
    comments = []
    dic = {'creds': creds, 'accs': accs, 'comments': comments}
    for fileName in ['creds','accs','comments']:        
        file = c.ROOT_URL + 'config/' + fileName + '_.txt'
        with open(file) as f:
            for line in f:
                dic[fileName].append(line.rstrip("\n"))
            f.close()
    return creds, accs, comments


def fetchLists(account: str):
    initialUsers = set()
    notFollowed = set()
    followed = set()
    privateRequested = set()
    with open(c.ROOT_URL + 'accounts/' + account + '/' + account + '_followers.csv') as followersFile:
        reader = csv.reader(followersFile, delimiter='\n')
        for user in reader:
            initialUsers.add(user[0])
        followersFile.close()    
    with open(c.ROOT_URL + 'accounts/' + account + '/' + account + '_not-followed.csv') as notFollowedFile:
        reader = csv.reader(notFollowedFile, delimiter=',')
        for user in reader:
            notFollowed.add(user[0])
        notFollowedFile.close()
    with open(c.ROOT_URL + 'accounts/' + account + '/' + account + '_followed.csv') as followedFile:
        reader = csv.reader(followedFile, delimiter=',')
        for user in reader:
            followed.add(user[0])
        followedFile.close()
    with open(c.ROOT_URL + 'accounts/' + account + '/' + account + '_private-requested.csv') as privateRequestedFile:
        reader = csv.reader(privateRequestedFile, delimiter=',')
        for user in reader:
            privateRequested.add(user[0])
        privateRequestedFile.close()
    return initialUsers, notFollowed, followed, privateRequested


# STRICT order of lists
def updateLists(account: str, notFollowedUsers: list, followedUsers: list, privateUsers: list):            
    genPath = 'accounts/' + account + '/' +  account
    nfPath = c.ROOT_URL + genPath + '_not-followed.csv'
    fPath = c.ROOT_URL + genPath + '_followed.csv'
    prPath = c.ROOT_URL + genPath + '_private-requested.csv'
    
    with open(nfPath, 'a') as notFollowedFile:        
        for userData in notFollowedUsers:
            for i in range(0, len(userData)):
                notFollowedFile.write(str(userData[i]))
                if (i + 1 == len(userData)):
                    notFollowedFile.write('\n')
                else:
                    notFollowedFile.write(',')
        notFollowedFile.close()
                
    with open(fPath, 'a') as followedFile:        
        for userData in followedUsers:
            for i in range(0, len(userData)):
                followedFile.write(str(userData[i]))
                if (i + 1 == len(userData)):
                    followedFile.write('\n')
                else:
                    followedFile.write(',')
        followedFile.close()       
                
    with open(prPath, 'a') as privateRequestedFile:        
        for userData in privateUsers:
            for i in range(0, len(userData)):
                privateRequestedFile.write(str(userData[i]))
                if (i + 1 == len(userData)):
                    privateRequestedFile.write('\n')
                else:
                    privateRequestedFile.write(',')
        privateRequestedFile.close()



# Randomness to prevent Instagram from detecting my automated activities            
def wait(n1: float, n2: float):            
    # default wait time 4 - 6 seconds
    if (n1 >= n2):
        time.sleep(randint(40000,60000)/10000)
    else:
        time.sleep(randint(n1 * 10000, n2 * 10000)/10000)        
 

def chanceOccured(chance):        
        if(randint(1,100) < chance):
            return True
        else:
            return False
       

def cleanNumber(stringNumber):
    tmpString = ''
    cnt = 0
    for letter in stringNumber:
        if(letter == '.'):
            continue
        if(letter == ','):
            cnt = 1
            continue
        if(letter == 'k'):
            if (cnt):
                tmpString = tmpString + '00'
            else:
                tmpString = tmpString + '000'
            continue
        if(letter == 'm'):
            tmpString = tmpString + '000000'
            continue
        tmpString = tmpString + letter
    stringNumber = tmpString
    print(stringNumber)
    return stringNumber
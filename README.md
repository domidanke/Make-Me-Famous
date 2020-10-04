![github-readme](https://user-images.githubusercontent.com/43521144/95005096-623a2b00-05b9-11eb-9edc-af0920b0408f.jpg)

# Make-Me-Famous
Using Instagram to automate user interaction

This Project's process is described as followed:
The User provides credentials, relatively popular Instagram Accounts, and a list of generic comments to be used

The Python User-Parse-"Bot" logs into Instagram, loops through all provided accounts, gets a list of roughly 1000 accounts following that popular account,
and then stores those users in a csv file saved in a directory per popular account.

The User-Processing-"Bot", afterwards, logs into Instagram and focuses on one popular account's followers that were previously stored in a list.
The Bot then loops through all user accounts, checks for public, private, posts, followers, and following, and determines whether this account
should be interacted with or not. The user stats are, again, stored in a csv file for future processing.

The Goal of this project is to get attention from a specific target of user accounts, pretend human interaction and genuine interests, and receive
recogition in the form of legitimate followers. The long-term goal is to make proper use of fetched data, increase quality of interactions,
and eventually CRACK the code of how to find and get the followers you want without actively spending hours and hours, and days and days to achieve this.



Let's get us started on the prerequisites:

Python 3+, Selenium, Chromedriver (has to match Chrome Version)

# Instructions to set up:

1. Install Python Version 3+
2. Install Chromedriver and add exe-file to PATH (Windows: https://www.youtube.com/watch?v=dz59GsdvUF8; Mac: https://www.youtube.com/watch?v=XFVXaC41Xac)
3. Install Selenium -> Console: pip install selenium
4. Find and edit the following file: "py/selenium/webdriver/common/action_chains.py" as followed:
 In lines 89-91, add the 2 line for-loop (This needs to be added to reset keyboard actions after each use; selenium lib will include this fix in the next version)
    
    if self._driver.w3c:
            self.w3c_actions.clear_actions()
            for device in self.w3c_actions.devices:
                device.clear_actions()
        self._actions = []
        
5. Locate comments, creds, and accs.txt-files in the config directory in the project and proceed as followed:
-> creds_.txt:    Enter your username and password in line 1 and line 2 respectively
-> comments_.txt: Enter a list of comments (one comment per line)
-> accs_.txt:     Enter a list of 'popular' user accounts that you aim to get followers from, again, one per line

6. For the initial User List, Run the following file: ParseAccounts.py
7. After the users are properly fetched and stored, run the following file after initializing the object ProcessAccountsBot() passing in one of the popular      accounts as a string

The Process Bot will then go through all the users from popular account x and like/comment/follow etc. in a very human-like fashion.


ENJOY!

import sys
sys.path.insert(1, '../classes/')
from processMainpageBot import ProcessMainPageBot

processMainpageBot = ProcessMainPageBot('dead.programmer')
processMainpageBot.watchStories()
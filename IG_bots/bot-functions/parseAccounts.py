import sys
sys.path.insert(1, '../classes/')
from parseAccountsBot import ParseAccountsBot


parseAccountsbot = ParseAccountsBot()

parseAccountsbot.parseThroughAccounts()
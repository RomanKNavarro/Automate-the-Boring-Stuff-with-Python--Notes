#! python3
# pw.py - An insecure password locker program


PASSWORDS = {'email': 'ocegueda22',
            'steam': 'pridetothegenocide',
            'hulu': 'laurel527'} 		# The keys can all be used as the command argument	

import sys, pyperclip
if len(sys.argv) < 2: 	                        # This program requires the user to type in a 'command argument'. This string will return if nothing is given
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
	

account = sys.argv[1]                           # sys() can accept multiple command arguments. Here, the account name that the user typed 
						# is being stored in the first and only command argument, "account".

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])		# This will copy the password to the clipboard
    print('Password for ' + account + ' copied to the clipboard.')
else:
    print('There is no account named ' + account)
 
# sys.argv is a variable containing a list in which all the command line arguments are stored

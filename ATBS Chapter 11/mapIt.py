#! python3
# mapIt.py - Launches a map in the browser using an address from the
# comand line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
   # Get address from command line.
   address = '+'.join(sys.argv[1:]) # The splice makes sure to not to use 'mapIt.py' in the string

else:
   # Get address from clipboard.
   address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + address)
   

# address = [address number and name, city, state, zip code]

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
   # Get address from command line.
   address = '+'.join(sys.argv[1:]) # The splice makes sure to not to use 'mapIt.py' in the string

else:
   # Get address from clipboard.
   address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + address)

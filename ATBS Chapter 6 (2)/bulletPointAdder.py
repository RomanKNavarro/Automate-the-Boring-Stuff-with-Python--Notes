#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start 
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')		 # The text is split whenever a '\n' character is found.
for i in range(len(lines)):		 # loops through all the indexes in the 'lines' list
	lines[i] = '* ' + lines[i]       # adds a star and space at the beginning of each string in the 'lines' list 
text = '\n'.join(lines)			 # The .join() method creates a single string from the values in 'lines'. 
		                         # Between each value a newline is added.
								    
pyperclip.copy(text)
print('Your new string awaits you in the clipboard')


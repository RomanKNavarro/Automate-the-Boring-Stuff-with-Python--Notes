#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # optional area code (either 3 digits or 3 digits encased in paretheses)
    (\s|-|\.)?                      # separator (either space, minus sign, or dot)             
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator (either space, minus sign, or dot)
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # optional extension (a space, followed by
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# Finds matches from the text pasted into the Clipboard 
text = str(pyperclip.paste())                               
matches = []
for groups in phoneRegex.findall(text):                                    
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # binds the area code and first/last digits with '-' using 'join()' 
    if groups[8] != '':                                    
        phoneNum += ' x' + groups[8]                       # If there is an extension, ' x' is applied first
    matches.append(phoneNum)                               # Any matches found are reconfigured with the format in 'phoneNum'
for groups in emailRegex.findall(text):                    
    matches.append(groups[0])                              # any email matches found are copied to the clipboard
                   
# Copies the new string into the Clipboard if 'matches' has more than zero values
if len(matches) > 0:                                
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or addresses found.')
                
               

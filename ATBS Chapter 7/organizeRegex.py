import re
    
phoneRegex1 = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

sadam = phoneRegex1.search('My phone number is 408.3349\)')
print(sadam.group() +'\n')

phoneRegex2 = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (either 3 digits or 3 digits encased in paretheses)
    (\s|-|\.)?                      # separator (either space, minus sign, or dot)             
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator (either space, minus sign, or dot)
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # optional extension (a space, followed by
    )''', re.VERBOSE)

salaam = phoneRegex2.search('My phone number is (209)-408-3349 ext. 958)')
print(salaam.group())

'''Long, complex regexes such as phoneRegex1 can be hard to read and interpret. Luckily, re.VERBOSE can be
passed as a second argument in re.compile(). This will cause the regex to enter what is called the
"verbose mode", which will cause re.compile() to ignore any whitespace and comments in the regex, enabling you
to warp the regex's contents to whatever alignment you find the best readable.'''

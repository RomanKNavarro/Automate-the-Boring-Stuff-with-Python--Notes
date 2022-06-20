#! python3
# numberExtractor.py - Matches number containing commas (From Practice Questions)

import re

num = re.compile('\d{1,3} | \d{1,3},\d{3}(,\d{3})?')
    

extr = num.search('As of now, I have 324,453 dollars')
print(extr.group())

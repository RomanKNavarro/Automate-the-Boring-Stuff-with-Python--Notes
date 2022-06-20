#! python3
# nakamotoEXtractor.py - Matches 'Nakamoto' (practice question)

import re

naka = re.compile(r'([A-Za-z.]+)?(\s)?(Nakamoto|nakamoto)')

finden = naka.search('Hello there,  Mr. nakamoto')
print(finden.group())


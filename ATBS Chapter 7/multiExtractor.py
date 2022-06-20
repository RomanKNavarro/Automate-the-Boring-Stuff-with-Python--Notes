#! python3
# multiExtractor.py - Matches multiple objects with the Pipe (practice question)

import re

multi = re.compile(r'''(
    (Alice|Bob|Carol)+
    \s
    (eats|pets|throws)+
    \s
    (apples|cats|baseballs)+
    )''',re.VERBOSE | re.IGNORECASE)

finden = multi.search('CAROL EATS CATS')
print(finden.group())


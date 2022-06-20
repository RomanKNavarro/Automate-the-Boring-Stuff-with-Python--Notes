# First code wars project

import re 

def disemvowel(string):
    vowel = re.compile('[aeiouAEIOU]')
    comment = vowel.sub(r'',string)
    string = comment
    return string

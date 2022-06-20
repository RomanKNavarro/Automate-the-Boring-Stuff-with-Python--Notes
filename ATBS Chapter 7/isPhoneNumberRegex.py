import re

phoneNumRegex = re.compile(r'd\d\d-d\d\d-d\d\d\d')
mo = phoneNumRegex.search('My number is 123-543-7322')
print('Phone Number found: ' + mo.group())


'''This program does the same as the previous PhoneNumber.py, except that this
one uses "regular expressions", or "regexes", for short. Using these
typically results in fewer code.'''

'''Note that in order to use regular expressions, the module 're' has to be
imported. Otherwise, Python will not recognise any 'regex' functions used.'''

''' 're.compile' is where the pattern for the regular expression will be
stored. This function, combined with the pattern, create a "regex object".
The pattern within a regex object represents the format that a regular expression
should follow. Since the pattern characters in the regex objects use
backslashes, it is convinient to call 'r' before typing the string, which will
prevent them from escaping. The "\d" characters in this regex object's pattern
represent digits'''

''' The regex method, ".search()", is passed a string that can potentially
contain the desired pattern for the regex. If the pattern of the regex object is
not found once "search()" has been called to the variable containing the regex
object, "None" is returned. Otherwise, a "match object" will be returned instead.
This match object is stored in the variable containing the ".search()" method, to
which the "group()" method is be called to. "group()" will then return any 
values that follow the pattern in the regex object.'''

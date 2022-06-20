# All the string methods found throughout chapter six will be stored here


'''the .upper() and .lower() methods are used to convert a string's
characters from lower-case to upper-case and vice versa'''

spam = 'Hello World!'
print(spam.upper())
print(spam.lower())
print(spam[0:5].lower(), spam[6:11].upper())
spam = spam.lower()
print(spam)

'''In this short program, the user's response is case-insensitive. It does not
matter how 'great' is typed. This is because the string 'great'was converted
to lowercase.'''

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
    
'''The isupper() and islower() methods return Boolean values indicating if a
string is completely uppercase or lowercase'''

x = 'check nuts before you step to these'
y = "MUTHUPHUCKIN REAL G'S"
print(x.islower())
print(y.isupper())

print('ON HIS OLD ALBUM COVERS'.lower())
print('he was a she thang\n'.upper().lower().upper())


''' Here are some more string methods, which, like the islower() and isupper()
methods, return Boolean values that describe a string's conditions'''


# isalpha() indicates if a string consists entirely of letters
dre = 'Drophiminhistracks'
print(dre.isalpha())

'''isalnum() indicates if a string consists only of letters and numbers. Will
return true even if the string contains only letters or only numbers'''
print('streets'.isalnum())
print('streets123'.isalnum())

# isdecimal() indicates if a string is entirely numbers
print('nineteen'.isdecimal())

# isspace() indicates if string is entirely spaces, tabs, and newlines
print("       \t \t \n \n \n \n      ".isspace())

# istitle() indicates if all letters in the beginning of each word
# is uppercase, while the rest of the letters are lowercase
print('THIS IS WURST'.istitle())
print('This Is Wurst'.istitle())


'''The startswith() method returns a boolean that indicates if a string begins
with a value that has been passed on to it as an argument, and the endswith()
method indicates if the string ends with the value.'''

print('take it into consideration'.startswith('take'))
print('I sure will do so'.endswith('soy'))
finnish = 'Mannerheim line'
print(finnish.endswith('lane'))
print(finnish.startswith('M'))


''' The .join() method takes a list of strings as it's argument. It returns the
concatenation of all the strings to create a single, longer string. The way
this this works is by the .join() method being inserted in the commas that
seperate each value in the list, combining them. The .join() method itself has
to be called onto a string value in order to work. This string value will then
repeat itself throughout the string that was combined with the list values'''

print(' '.join(['this', 'is', 'my', 'top', 'priority']))
print('$$$$'.join(['I', 'WILL', 'NOT', 'LOSE']))
sweetener = ' fucking '
tea = ['I', 'hate', 'jews', 'Every', 'single', 'one\'s a', 'pig']
print(sweetener.join(tea))


'''.split() does the oposite of the .join() method. It is called onto a string,
which it then splits into smaller strings and places them in a list. If given an
argument (a string value), it will remove this value from the string.'''

print('DasistHitlerundseinkrieg'.split())
print('$$$$N$$$$$$I$$$$$$$$$G$$$$$$G$$$$$$$$E$$$$$R$$$'.split('$'))

prologue = '''This is
what you thought it wasn't
it beez
the brothers representing the dirty dozen
I be the FROGG
and here's my man
he goes by the name of errr...'''

print(prologue.split('\n')) 
''' ^^^ This will split the multi-line string along the newline characters.
Each value in the returned list will therefore correspond to each line.'''

''' rjust() and ljust() return a more-spaced out (justified) version of the
string it was passed down, with the former spacing the string out to the right
and the latter to the left. The integer that is passed down to them as an
argument determaines the amount of times that the string will be spaced out.
The center() method is spaced out on both sides. Unlike the other two, the
center() method can take an extra argument. This one lets the user choose the
character they wish to use for the spacing-out'''

print('This the east,'.rjust(30))
print('this the west'.ljust(30))
print('and this south central\n'.center(30,'$'))


''' Removing any whitspace from the left or right side of strings can be done
using the rstrip() and lstrip() methods, respectively. To remove the whitespace
from both sides simultaneously, the strip() method can be used instead. These
methods also accept arguments that specify which characters should be removed
from the string's ends.'''

print('              How you doin?          '.strip())
print('              How I\'m doing what?'.lstrip())
print('It was a question, sir'            .rstrip())
swine = 'SWINESWINESWINESWINElearn to talk, you uncultured swine!'
print(swine.strip('INSEW'))













































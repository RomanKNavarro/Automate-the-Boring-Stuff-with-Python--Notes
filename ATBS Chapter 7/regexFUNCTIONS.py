import re

# Grouping With Parentheses

number = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchedOBJ = number.search('Call 188-882-04563 now')

print(matchedOBJ.group(1))
print(matchedOBJ.group(2))
print(matchedOBJ.group(0) + ' is my phone number\n')

''' regex patterns can be organized into seperate 'groups' by using parentheses.
Each group can be called using the 'group()' method with it's corresponding
number as the argument. Assigning 0 or nothing to group() will print the entire
string. In terms of phone numbers, grouping is useful if the area code has to be
separated from the rest of the numbers.'''

print(matchedOBJ.groups())
areaCode, number = matchedOBJ.groups()
print('The area code is ' + areaCode + ' and the rest is ' + number + '. Bye. \n')

''' The 'groups()' method will return a tuple containing the groups in the regex.
This makes it possible to use the 'multiple assignment trick', in which numerous
variables are assigned to the values in the tuple simultaneously.'''

number = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
matchOBJ = number.search('Call (188) 832-4322 right now')
print('The area code is ' + matchOBJ.group(1) + ' and the rest is ' + matchOBJ.group(2))
print(matchOBJ.group() + ' is the number.\n')
      
''' If the regex requires parentheses, the '\(' and '\)' escape characters have to
be passed to re.compile(). These can be used to separate the area code from the rest
of the phone number.'''

# Matching Groups with 'Pipe'

guay = re.compile(r'Uruaguay|Paraguay')
first = guay.search('Uruaguay and Paraguay are in South America')
print(first.group())
second = guay.search('Paraguay and Uruguay are in South America')
print(second.group())

guays = re.compile(r'(Para|Uru|Peru)guay')
matchObj = guays.search('Paraguay is a shithole monkey country')
print(matchObj.group() + ' is a country I never want to visit.\n')

''' The 'pipe' symbol (|) is used to match one of several expressions from the regex.
If multiple pipe characters are found in a string, the one that makes the first appearance
will be returned by group().'''

# Optional Matching with the '?' symbol

stans = re.compile(r'alt-right (neo-)?nazis')
object1 = stans.search('Those were alt-right nazis')
print(object1.group())

object2 = stans.search('Today they are called alt-right neo-nazis')
print(object2.group() + ' saved my life from the treacherous jew\n')

''' If there is a pattern that should be found optionally, it is placed inbetween
parentheses and a '?' is added.'''

''' To create an optional object in the regex, place it in any desired location
and encase it with parentheses and add a question mark to the right. If an actual
question mark needs to be used in the regex, use the '\?' escape character'''

# Optional Matching with the '*' symbol

multiple = re.compile(r'(Stan)* The Man')

stan = multiple.search(' Stan The Man stole my wallet')
print(stan.group())

stan2 = multiple.search('Stan Stan Stan The Man')
print(stan2.group())

stan3 = multiple.search('Where can I find StanStanStanStan The Man')
print(stan2.group(), 'killed his pregnant wife\n')

''' Unlike the previous method using the '?' symbol, using the '*'
symbol in the regex will match the optional text however many times
it is used. If an actual star character is required in the regex, use '\*',
as simply using '*' will cause the character to escape.'''

# Matching with the '+' symbol.

fall = re.compile(r'(rosa)+ schweinefleisch')

pork1 = fall.search('Ist das schweinefleisch rot oder rosa?')
print(pork1 == None)

pork2 = fall.search('Ja, das ist rosa schweinefleisch')
print(pork2 == None)
print(pork2.group())

pork3 = fall.search('Ja, das ist rosarosarosarosa schweinefleisch')
print(pork3.group() + '? gut\n')

''' Matching with the '+' symbol is similar to matching with the '*' symbol,
except that this form of matching requires the encased group to appear at least
once in the string, otherwise, the string will not be matched. Therefore, this
is not a form of "optional matching".'''

# Matching Repetitions with Curly Brackets

worth = re.compile(r'\d{7,}')
print('Welcome to the Mega-Synagogue. What is your net-worth?')
response = worth.search('3005435543 dollars')
print(response.group() + ' dollars? Hop on board!')

no = re.compile(r'n(o{10,50})')
print('What did Vader say after breaking free?')
yell = no.search('noooooooooooooooooooooooooooooooooo')
print(yell.group())

start = re.compile(r'(ja){2}')
print('How do you say slut in german?')
slut = start.search('du ist eine jaja')
print('Nein! DU IST EINE ' + slut.group())

million = re.compile(r'1(0{6})')
jewish = million.search('I have 1000000 dollars')
print('I too, have ' + jewish.group() + ' dollars , yet I am not jewish\n')

''' Matching with curly brackets is used when there is a string value that needs to be
repeated a specific number of times. The string is encased in parentheses and the integer
is encased in brackets, which determines the exact number of times this string should be
repeated. When 2 integer values are used in the brackets, they are separated with a comma.
The first value indicates the minimum amount of times the string should be used and the
second one indicates the maximum. Either of these values can be left blank if a minimum or
maximum isn't needed.''' 

# Greedy and Non-Greedy Matching

lolen = re.compile(r'(HA){3,5}')
jaja = lolen.search('That funny. HAHAHAHAHA.')
print(jaja.group())

lolen = re.compile(r'(HA){3,5}?')
jaja = lolen.search('That funny. HAHAHAHAHA')
print(jaja.group() + ", oh you're funny\n")

''' When using 2 integers in curly brackets, Python will always search for the longest possible
repetition in the passed string. Here, for example, while HAHAHA, and HAHAHAHA are
valid matches, Python decides to return HAHAHAHAHA, the longest possible match. This is because
regular expressions are 'greedy', by default. To use the 'non-greedy' version of repetion matching,
a question mark has to be added after the curly brackets. This will result in group() returning the
shortest repetition available in the regex, no matter how long it actually is. This question mark
isn't to be mistakened with the one used in optional matching.'''

# The 'findall()' Method

ages = re.compile(r'\d(\d)?')
members = ages.search('Cole is 3, Marie is 10, and Jorgesten is 14')
print(members.group())

ages = re.compile(r'\d+')
members = ages.findall('Cole is 17, Marie is 20, and Jorgesten is 24')
print(members)

ages = re.compile(r'(\d)(\d)?')
members = ages.findall('Cole is 14, Marie is 27, and Jorgesten is 30')
print(members, '\n')

''' The search() method will only return the first match object found in the string. The 'findall()'
method, however, will find all the matched objects in the string and return them as strings
in a list. If the regex contains groups, then a list of tuples will be returned instead. Each tuple
represents a found match, and the strings within them represent groups. Note that this function returns
strings of the matched objects, rather than the matched objects themselves, like search(). '''
                        
# Character Classes

xmasRegex = re.compile(r'\d+\s\w+')
items = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds')
print(items)

email = re.compile(r'\w+\@\w+.com')
quantity = email.findall("Joseph's email is joejoe@gmail.com and Rudolpho's is gaydolfo@fagmail.com")
print(quantity, '\n')

''' Here, 2 new character classes are used. The first is the '\s' character, which signifies any space, tab, or newline
character, and the '\w' character, which signifies any letter, numeric digit, or underscore character. When a '+'
symbol is used on these character classes, one or more of the specified characters can be used. For example, in '\d+',
one or more digits that range from 0 to 9 can be used.'''

# Making Your Own Character Classes

vowels = re.compile(r'[aeiouAEIOU]')
juden = vowels.findall('achtung, juden. ACHTUNG JUDEN!')
print(juden)

score = re.compile(r'[\d:\d]')
games = score.findall("The score last night was 1:3. Experts predict that tonight's will be be either 2:3 or 1:2.")
print(games)

secret = re.compile(r'[^!D@#*%&$H]')
message = secret.findall('$%#D%$N$%@%$H&*$U*&%D%$#%#&H**&%$#%T!H@D')
print(message, '\n')

''' If the character classes already provided by Python aren't enough to suit your needs, new ones can be created instead.
To define your own character classes, they must be encased in square brackets, '[]'. In here, all the characters that you
wish to be matched are stored. Using the '^' symbol on character classes will cause findall() to return any characters
from the string that are not in the character class. The '-' symbol is used to create ranges for both letters and numbers'''

# Using The ^ And $ Symbols

print('What is your name?')
start = re.compile(r'^My name is ')
intro = start.search('My name is Gustav Klimt')
print(intro.group())

print('What is your net worth?')
cash = re.compile(r'dollars$')
worth = cash.search('As of yesterday, I am worth 2.1 billion dollars')
print(worth.group())

print('What is your social security number?')
wholeStringIsNum = re.compile(r'^\d+$')
czech = wholeStringIsNum.search('56764535325432') 
print(czech.group(), '\n')

''' The ^ symbol is added at the beginning of the regex to find a match
that occurs only at the start of the string, while the $ symbol is added
at the end of the regex to to find a match that occurs only at the end
of the string. Both symbols can be added to the regex to indicate that
the entire string passed to search() must match the pattern''' 

# Matching With ".", ".*", ".*?", and re.DOTALL

stanREGEX = re.compile(r'.istan')
ca = stanREGEX.findall('Pakistan Turkmenistan Afghanistan Kazakhstan Uzbekistan')
print(ca)

stanREGEX = re.compile(r'.*istan')
ca = stanREGEX.findall('Pakistan Turkmenistan Afghanistan Kazakhstan Uzbekistan')
print(ca, 'are all in Central Asia')

greedy = re.compile(r'(.*)') 
man = greedy.search('(Switzerland) is where I am from .)')
print(man.group())

nongreedy = re.compile(r'\(.*?\)')
man = nongreedy.search('(Switzerland) is where I am from.)')
print(man.group() + '\n')

noNewLine = re.compile('.*')
noSearch = noNewLine.search('Relax and take notes,\n as I take tokes of the marijuana smoke')
print(noSearch.group())

yesNewLine = re.compile('.*', re.DOTALL)
yesSearch = yesNewLine.search('as I take tokes of the marijuana smoke,\nThrow you in a choke,\ngun smoke gun smoke')
print(yesSearch.group(), '\n')

''' The dot character, '.', also called the 'Wildcard' will return a single character per match object in the string, with the
exception of newlines.

To match all of the characters per match object, the dot-star (.*) has to be used instead. Note that the dot-star, like repetition
matching with curly brackets, is greedy by default, and will try to match as much text possible in the search() string.

Once again, the "?" symbol has to come into play, this time in the form of the dot-star-question mark (.*?), which will match the
shortest valid string possible. If a newline has to be matched, 're.DOTALL' has to be passed as a second argument in the regex.'''

# Case-Insensitive Matching With re.IGNORECASE

egg = re.compile(r'easter egg', re.IGNORECASE)

easter = egg.search('I found an eaSTER eGG')
print(easter.group())

brick = egg.search('I smashed the EASTer Egg on his head')
print(brick.group(), 'is a valid match object\n')

''' The 're.IGNORECASE' method will make the regex case-insensitive.
A match can be typed with either upper or lower case letters, just as
long as the word itself is the same. note that 're.I' can also be used.'''

# Using the 'sub()' Method to Substitute Strings

government = re.compile(r'killed(\w+)?')
print(government.sub('brought to justice', 'Jermaine Dupri was killed by police for alleged drug possession. His other companions, too, were killed.'))

mrRegex = re.compile(r'Mr. (\w*) (\w)')
print(mrRegex.sub(r'Mr. \2', 'Mr. Erich Schukulwergen was murdered by Mr. Josef Gloptenstupel, who was then murdered by Mr. Otto Nochtiseitzer\n'))

''' 'sub()' is a method that requires an extra argument, which is a string
that will substitute any regex matches found in the larger string. If there are
groups in the regex, they can be passed to the extra argument in the form
of their corresponding numbers, \1,\2,\3, and so on. This will result in
the contents of the group(s) to be printed in the string, while the rest
of the other groups won't.'''

# Combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE methods

allMethods = re.compile(r'''(
    \d{2,4}         # address number
    \s\w\.          # space, followed by a single character and dot
    \s\w*           # another space, followed by multiple characters (street name)
    )''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

print(allMethods.findall('My address is 890 N. Hucklefruit. \n His address is 536 W. Yorkshire.'))


''' To use re.IGNORECASE, re.DOTALL, and re.VERBOSE in the same re.compile function,
the '|' separation character has to be used. In this context, this character would be
called the 'bitwise or' operator.'''
































































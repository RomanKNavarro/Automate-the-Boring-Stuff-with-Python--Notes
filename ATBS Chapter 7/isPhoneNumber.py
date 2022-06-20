# This program checks if a string is a phone number, without the use of 'regular expressions'

def isPhoneNumber(text):
    if len(text) != 12:                 # Checks that the string is 12 characters long
        return False
    for i in range(0, 3): 
        if not text[i].isdecimal():     # Checks if the first 3 characters are all numbers
            return False
        if text[3] != '-':              # Checks if the 3rd character is a hyphen
            return False
        for i in range(4, 7):
            if not text[i].isdecimal(): # Checks if the next 3 characters are all numbers
                return False
        if text[7] != '-':              # Checks if the 7th character is a hyphen
            return False
        for i in range(8, 12):       
            if not text[i].isdecimal(): # Checks if the last 4 characters are numbers
                return False
        return True

print('432-476-7654 is a phone number:')
print(isPhoneNumber('432-476-7654'))
print('Moshi Moshi is a phone Number:')
print(isPhoneNumber('Moshi Moshi'))

message = 'Call me at 321-432-5434 tomorrow.543-654-4324 is my office.'

for i in range(len(message)):
      chunk = message[i:i+12]                     
      if isPhoneNumber(chunk):                     
          print('Phone number found: ' + chunk)
print('done')

'''This for loop, using 'chunk', iterates through every character in the string, adding 11 characters
in front of it (12 in total). The 'isPhoneNumber' function then goes through each of these iterations,
and determines if any of them meet the requirements to be considered a phone number.'''





# Small Project for better understanding

def isPhoneNumber(text):                
    if len(text) != 12:                 
        return False                    
    for i in range(0,12):
        if not text[i].isalpha():
            return False
    return True

'''This function determines if 'text' meets certain requirements, which are: whether or not 'text' is 12
characters long, and if it is purely composed of letters'''


lageren = 'I am fucking jewisch werecanifind the asdfghjklmnb and the asdweqewewds'
for i in range(len(lageren)):
    neger = lageren[i:i+12]
    if isPhoneNumber(neger):
        print('founded: ' + neger)
print('jewish')

''' For every character in the string, neger will add 11 more characters in front of it, resulting in 12 total
characters. 'isPhoneNumber' will then determine if any of these iterations meet any of the requirements in it's
local scope





































    

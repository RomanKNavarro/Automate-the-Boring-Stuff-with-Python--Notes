# "Truthy" and "Falsey" values

name = '' # name is equal to anything
while not name: # the 'not' will reloop the print statement if nothing was entered
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input()) # If a number isn't typed, an error message will appear
if numOfGuests: # if zero is typed, the print statement will be skipped
    print('Be sure to have enough room for all your guests.')
print('Done')

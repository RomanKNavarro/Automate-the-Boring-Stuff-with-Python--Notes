# passingReference.py
print()
print('passingReference.py:')
print()


def eggs(someParameter):
    someParameter.append('Hello')       # reminder, the append() method adds a new value to the end of a list. Also, append() does not return the new value of spam, as it already modifies the list in place.

spam = [1, 2, 3]
eggs(spam)                              # when the 'eggs()' function is called, the values of the argument, 'spam', are passed to the parameter, 'someParameter'.
print(spam)

snot = ['Hallo', 'Bonjour',]
eggs(snot)
print(snot)




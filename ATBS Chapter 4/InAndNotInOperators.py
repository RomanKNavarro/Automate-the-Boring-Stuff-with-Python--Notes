# the 'in' and 'not in' Operators are used to determine if whether or not an item is in a list
# a better example, see the rockpaperscissors project.


myPets = ['Zophie', 'Pooka', 'Fat-Tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)   # prints if the given name is not found in the list
else:
    print(name + ' is my pet.')                  # prints otherwise

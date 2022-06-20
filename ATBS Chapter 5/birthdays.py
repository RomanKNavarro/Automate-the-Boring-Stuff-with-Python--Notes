birthdays = {'April': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:                                           # This takes effect if the typed name is one of the keys in the dictionary. If not, then the else statement will trigger instead.
        print(birthdays[name] + ' is the birthday of ' + name)      # 'birthdays[name]' will print the value stored in the key, which will be the birthday, and 'name' will print the key itself, the name of the person.
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday                                      # This will store the new person's birthday to the dictionary temporarily, and will print the given birthday if said person's name were to be typed again
        print('Birthday Database updated.')                         # The information for any new people will be deleted from the 'database' once the program is closed. 

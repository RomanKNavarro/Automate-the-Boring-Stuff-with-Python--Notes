# keys(), values(), and items() are all dictionary methods that return list-like values of the dictionary's contents.
# Note that the values returned by these methods are immutuable.


# The first program uses the values() method, which iteriates over the values (not keys) of a dictionary.
# The second one iterates over the keys, by using the keys() method, and the third one uses the items()
# method, which iterates over both values and keys.

spam = {'color': 'brown', 'age': 42}
for v in spam.values():
    print(v)


for k in spam.keys():
    print(k)


for i in spam.items():          
    print(i)                # This will print a tuple containing the values, rather than a list.





# To have a list value returned by any of these methods, and not a tuple, the list() value has to be used:

spam = {'color': 'red', 'age': 42}

print(spam.keys())          # dict_keys(['color', 'age']) is printed rather than just the list itself
print(list(spam.keys()))    # prints just the list





# The Multiple Assignment Trick can be used in a 'for' loop to assign the key and value to seperate variables:

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():                       # Here, the 'color' and 'age' keys are assigned to the 'k' and 'v' variables, respectively.
    print('Key: ' + k + ' Value: ' + str(v))





# Just like in Lists, the 'in' and 'not in' operators can be used to determine if whether or not a certain key or value exists in a dictionary:

quantitties = {'Iron': '1%', 'Calcium': '21%', 'Lime': '64%'}

print('1%' in quantitties.values())
print('1%' in quantitties.keys())
print('Calcium' in quantitties)
print('Lime' not in quantitties)
print('Protein' not in quantitties)




# The get() method can take two arguments at once. The first one is the key of the value that will be used, and the second one is a back-up value to be called
# instead, should the first value not exist in the dictionary.

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups')) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')    # Since there is no 'eggs' key in the dictionary, the alternative value is printed instead.





# The setdefault() is a method that is used to add new key-value pairs to a dictionary. If a given key already exists in the dictionary but it's value is different,
# no changes will be made to it.

centralcapitals = {'Germany': 'Berlin', 'Switzerland': 'Geneva', 'Denmark': 'Copenhagen'}

centralcapitals.setdefault('Austria', 'Vienna')
print(centralcapitals)

centralcapitals.setdefault('Austria', 'Mozart')
print(centralcapitals)

centralcapitals.setdefault('Germany', 'Frankfurt')
print(centralcapitals)














































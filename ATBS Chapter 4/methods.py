# METHODS!!!!!!!!
# The following are methods. More accuratly, they are list methods, meaning that they cannot be used elsewhere other than list values. if they are used on
# strings or integers, for example, the 'AttributeError' will return, and will print a message like "'str' object has no attribute 'append'".
print()
print('Methods:')
print()


# The first Method to learn is the 'index()' method. Just as it's name suggests, it converts a given item to it's index.

realOGs = ['Ali', 'Foreman', 'Frazier', 'Liston']
print(realOGs.index('Foreman'))
print(realOGs.index('Liston'))

# If there is a duplicate item in the list, index() will return the index of it's first appearance.

realOgs = ['Ali', 'Ali', 'Frazier', 'Liston']
realOgs.index('Ali')
print(realOgs)


# There are 2 methods that can be used to add new items to a list. The first is 'append()', and the second is 'insert()'.

# 'append()' will add a new item to the end of the list:
RIPogs = ['phifedawg', 'biggie', 'flava', 'odb']
RIPogs.append('prodigy')
print(RIPogs)

# 'insert()' will add a new item to any given index, without removing any other items:
RIPogs = ['phifedawg', 'biggie', 'flava', 'odb']
RIPogs.insert(1, 'prodigy')
print(RIPogs)

# Note that neither of these methods will return the new value of 'RIPogs' when they are called. Instead the modified list needs to be called with 'print()'.


# items can be removed with 'remove()'. This is used when you forgot the index of an item, but know it's name;
# the 'del' statement is used when you don't know the item name, but know it's index (e.g: 'del wutang[3]')

wutang = ['Raekwon', 'Method', 'Inspectah', 'OBD','GFK', 'RZA', 'Jizza', 'Nas']
wutang.remove('Nas')
print(wutang)

# If remove() is used on a duplicate item, it's first appearance is deleted:

wutang = ['Raekwon', 'ODB', 'Method', 'Inspectah', 'OBD','GFK', 'RZA', 'Jizza']
wutang.remove('ODB')
print(wutang)


# 'sort()' is used to organize the order of items. If there is a set of numbers in a list, sort() organizes them from least to greatest.
# If it is strings in a list, sort() organizes them by alphabetaical order. 'sort()' cannot be used on a list that contains both strings and numbers

numbers = [5,2,3,1,4]
numbers.sort()
print(numbers)

letters = ['zombie', 'dracula', 'frankenstein', 'werewolf']
letters.sort()
print(letters)

# If 'True' is passed to the 'reverse' keyword in sort(), the values will be re-organized in the opposite order.

numbers = ['hello', 'ali', 'shaheed', 'wehrmacht']
numbers.sort(reverse = True)
print(numbers)

letters = ['zombie', 'dracula', 'frankenstein', 'werewolf']
letters.sort(reverse = True)
print(letters)

# 'sort()' uses the "ASCIIbetical order" instead of the standard alphabetical order when it comes to strings.
# This means that uppercase letters come before lowercase letters, no matter what.

specialty = ['A', 'b', 'C', 'd', 'E', 'f', 'G']
specialty.sort()
print(specialty)

# to have 'sort()' organize string items in regular alphabetical order, 'str' needs to be passed.

specialty.sort(key=str.lower)
print(specialty)

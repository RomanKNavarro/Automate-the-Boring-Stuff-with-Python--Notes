# Introduction to lists:
print('Intro to Lists')
print()

# A list is a value which itself contains multiple other values, organized by an ordered sequence, and enclosed with brackets. The values inside a
# list are called 'items'. The items are seperated by commas, which means that the items are 'comma delimited'. Lists can be stored in
# variables, making them easier to assign to functions and other variables. Each item in a list is ordered starting from zero and going up.
# For example, if there is a list that has been assigned to a variable named 'jose', then the first item in the list would be called jose[0].
# The number in the bracket is called the 'index'. If an index number exceeds the number of items in a list, the IndexError will be given.
# Also, indexes can only be integers, meaning that something like 'jose[2.0] will cause an error, that is, the TypeError.



# the list itself
['taco', 'burrito', 'torta','黑鬼']

# the list being assigned to a variable
jose = ['taco', 'burrito', 'torta', '黑鬼']



# the list being printed
print(jose)

# items being printed using their indexes
print()
print('items being printed using their indexes:')
print()



print(jose[0])
print('chicken ' + jose[1])     
print(jose[2])
print(jose[0], jose[1], jose[2])
print(['taco', 'burrito', 'torta'][2])
print('give me a ', jose[0])
print('the ', jose[3], 'stole my ', jose[2])

# indexes can also be negative. Instead of starting with 0 on the left and up, they start with -1  from the right and down.
print('the ', jose[-1], 'also stole my', jose[-4])



# Using len() on a list will return the number of items that it contains.
print()
print('len() on lists:')
print()

print(len(jose), 'is the length of "jose"')



# lists can be stored in other lists
print()
print('lists can be stored in other lists:')
print()


jose = [['taco','burrito','torta'],['Aaxis','Baxis','Xaxis','Yaxis']]
print(jose[0])      # instead of printing 'taco', the entire first list is printed instead, which would be considered an item on it's own.
print(jose[1])      # prints the second list
print(jose[-1])     #also prints the second list


# To print individual items inside the lists, 2 indexes have to be used. The first one is for the list, and the second one is for the item in the list.
print(jose[0][2])
print(jose[-1][-4])
print('The', jose[0][-2], 'is at the', jose[1][2],', and the', jose[-2][-1], 'is at the', jose[-1][-1])




# Removing Items Method 1:
# To remove items from a list and create 'sublists', 2 integers *not indexes* are used with the list variable, which are separated by a colon and incased in brackets.
# The first number indicates where the 'Slice' begins and the second where it ends. Keep in mind that the item in the second index is not included in the slice.
print()
print('Removing Items Meethod 1: Slices')
print()


russland = ['Romanov', 'Schtalin', 'Yakov', 'Rasputin']
print(russland)

print(russland[0:4])    # This slice begins with the first item and ends with the last. Therefore, all of the items are printed.
print(russland[:])      # since no integers are given on where to start or end the slice, no slice occurs, so the list remains whole.
print(russland[0:2])    # This slice starts with 'Romanov' and ends with 'Yakov'. Since the latter is the second integer, '2', it is not included in the slice.
print(russland[:2])     # Python accepts this empty left integer as '0'.
print(russland[1:4])    # While there isn't any fourth index,the last item is printed anyways.
print(russland[-3:-1])




# Removing items Method 2:
# Unlike slices, using 'del'statements on items will get them permanently removed.
print()
print('Removing Items Method 2: "del" statements')
print()

snacks = ['apple', 'schokolade', 'bannana', 'noodle']
print(snacks)

del snacks[3]
print(snacks)

del snacks[-3]
print(snacks)




# To change the items in a list, first select the index of the item you wish to modify, then assign it the name of your choosing.
print()
print('Changing items using indexes:')
print()


nsdap = ['Himmler','Goring','Goebbels', 'Ludendorff']
print(nsdap)

nsdap[0] = nsdap[3]
nsdap[1] = nsdap[2]
nsdap[2] = 10           # integers are accepted, without the need of str() or quotes ''.
nsdap[-1] = 'Burgers'

print(nsdap)




# Using the + operator on 2 or more lists will combine and create a larger list. Using the * operator (Multiplication) on a list will replicate it's
# items in a single list. Be mindful that lists can not be multiplied with eachother.
print()
print('List Concatation and Replication:')
print()




# Concatenation
print(['pig', 'cow', 'snail'] + ['sheep', 'goat', 'satan'])

saintjudas = ['Alpha','Beta','Tango']
gustav = ['Charlie','Bravo','Foxtrot']
print(gustav + saintjudas)

massappeal = [1,2,3] + [4,5,6]
massappeal2 = [7,8,9] + [10,11,12]
print(massappeal + massappeal2)

materials = ['pen', 'paper', 'ink']
print(['paperclip', 'pencil', 'sharpener'] + materials)

# Replication
print(['Vear', 'ist', 'zhe', 'jude'] * 2)

meinneger = ['jump', 'jump', 'jump']
print(meinneger * 6)

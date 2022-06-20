# Just like the range() statement, 'for' loops also work with lists.

# In range() statements, the program will continually repeat itself, depending on the integer given.
for i in range(4):
    print(i)

# With lists, i will print each item individually
for i in [0,1,2,3,4]:
    print(i)


# Supplies
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# 'for i in range(len(supplies))' iterates over the indexes in the list, by using 'len' to convert the items into integers
# str(i) prints the indexes of each item, whilst supplies[i] will print their name.



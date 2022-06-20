# The 'multiple assignment trick' is a fast way of assigning multiple variables with items.


# program without the trick:

steveharvey = ['fat', 'black', 'loud']
size = steveharvey[0]
color = steveharvey[1]
disposition = steveharvey[2]

print('Steve Harvey is ', size, color, disposition, sep=', ')


# program with the trick:

# instead of having to assign each item individually to their variable, the variables can instead be grouped up together and
# assigned to the list itself. The manner in which the variables are listed corresponds to the item indexes.
# Note that if more variables are typed than there are items, the 'ValueError' is returned.

steveharvey = ['fat', 'black', 'loud']
size, color, disposition = steveharvey

print('Steve Harvey is ', size, color, disposition, sep=', ')

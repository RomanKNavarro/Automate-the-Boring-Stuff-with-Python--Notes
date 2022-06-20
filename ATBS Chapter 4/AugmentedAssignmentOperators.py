# Augmented Assignment Operators



# When adding to a number assigned to a variable, you would usually do the following:

spam = 42
spam = spam + 1
print(spam)


# As a shortcut, you can use an 'Augmented Assignment Operator (AAO)' instead:

spam = 42
spam += 1
print(spam)


# The '+=' AAO can also do string and list concatenation:

spam = 'Hello'
spam += ' world!'
print(spam)


# The '*=' (multiplication) AAO can do string and list replication:

bacon = ['Zophie']
bacon *= 3
print(bacon)

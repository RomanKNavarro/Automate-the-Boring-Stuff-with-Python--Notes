# Introduction to the Dictionary Data Type

steveharvey = {'size': 'fat', 'color': 'black', 'desposition': 'loud'}

print('steve harvey is ' + steveharvey['color'])

# This dictionary, above, was assigned to the variable, 'steveharvey'. Dictionaries look similar to lists, except that dictionaries have braces instead of brackets, and they also use what are called 'keys',
# which are the the dictionary equivalent to an index used in lists. However, while list indexes are limited to only sequenced integers, dictionary keys can use all other data types, such as strings and floats.
# The keys in the above example would be 'size', 'color', and 'desposition'. The names assigned to these keys are their values. A key, along with it's value, would be called a 'key-value pair'. 




spam = ['cats', 'dogs', 'jews']
bacon = ['cats', 'dogs', 'jews']

print(spam == bacon)

# In order for a list to be equal to another list, not only do the items have to be the same, but they have to be in the same order as well. If not, then 'spam == bacon' would be false.



spam = {'George': 'Washington', 'Benjamin': 'Franklin', 'Abraham': 'Lincoln'}
BrandenBurg = {'Abraham': 'Lincoln', 'George': 'Washington', 'Benjamin': 'Franklin'}

print(spam == BrandenBurg)


# This is not the case with dictionaries, however. The sequence of the pairs does not matter. As long as the values and keys are all the same, 'spam == BrandenBurg' will always be true.
# This is because there is no order sequence when it comes to dictionary items. For example, the first item in a list would be something like spam[0]. But in dictionaries, there isn't any 'first item'.
# Because of this unorderly nature, dictionaries cannot be sliced like lists. 


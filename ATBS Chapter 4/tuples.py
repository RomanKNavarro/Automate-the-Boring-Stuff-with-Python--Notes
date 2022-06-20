# The Tuple Data Type is similar to the List Data Type, except that it is immutable, like the string Data Type. Also, Tuples use parantheses () rather than brackets [].
print()
print('Introduction to The Tuple Data Type:')
print()


spontaneous = ('beechwood', 'probation', 3.42,)
print(spontaneous[2])
print(spontaneous[-2])

spontaneous2 = ('jewcrew',)  # If there is only one value in a tuple, a 'trailing comma' needs to be added afterwards in the parantheses, otherwise, python will not recognise this as a tuple.
print(spontaneous2[0])

# There are two main reasons why Tuples are used instead of Lists. First off, they are intended to be used when you want a an ordered sequence of values that you do not plan on changing, and this
# will let anyone else reading your code know as well. And second, due to their immutable nature, Python can optimize code using Tuples and make it run faster than code using lists.




# Data Types can be converted using the list() and tuple() functions.
print()
print('the list() and tuple() functions:')
print()


animals = ['cat','dog','bird']
print(tuple(animals))


juden = ('nestle', 'dell', 'seinfield')
print(list(juden))

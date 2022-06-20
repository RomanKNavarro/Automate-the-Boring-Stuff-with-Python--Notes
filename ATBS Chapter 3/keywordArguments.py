print()
print('Keyword Arguments:')
print()

# Some functions can optionally use certain parameters to create 'keyword arguments' .
# For example, print() has the 'end' and 'sep' parameters

# The 'end' parameter disables the newline that gets added at the end of print(), causing both statements to print on a single line
print('Hello')
print('World')

# By default, multiple strings in a single print statement will automatically space out
print('cats', 'dogs', 'mice')

# sep= can be added to separate each string with a comma
print('cats', 'dogs', 'mice', sep=',')

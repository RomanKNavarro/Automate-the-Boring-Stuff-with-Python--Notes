letter = '''Dear Alice,

Eves's cat has been arressted for catnapping, cat burglary, and extortion,

Sincerely,
Bob'''

print(letter)

''' Triple quotes are used
for strings that span multiple lines.
This also applies for comments '''


'''Just like lists, indexing, slicing, and
'in' and 'not in' operators also work with strings'''

print(letter[0])
print(letter[-2])
print(letter[11:42])

greeting = letter[0:10]
print(greeting)

print('cat' in 'catnapping')
print('cat' in 'cat')
print('cat' in 'dog')


# Indentation Exceptions



# Indentation and line spacing does not matter when it comes to lists.
# As long as the items are inbetween the brackets, Python will accept them as lists.

spam = ['apples',                                'figs',
    'oranges',

                                    'bananas',
'cats']

print(spam)



# A single instruction can be split across multiple lines by using the line continuation character, '\'.
print()
print('using the "\" line continuation character:')
print()


print('Auf das heibe bluht ein ' + \
      'kleines blumelein')


spam = 100000000000
spam += spam + spam - spam \
        /spam % spam

juden = None
if juden \
      == None:
      print('good job')

print('spam is equal too....' \
      + str(spam))

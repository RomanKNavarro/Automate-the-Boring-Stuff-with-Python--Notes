# vampire2.py

name = 'Scheisse'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, Grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
# When handling elif statements, python goes through them from top to bottom. Once it finds an elif statement that
# corrosponds to the 'age' value, it will select it, and automatically skip any other elif statements. In this case,
#'age' has been set to 3000. Instead of selecting the vampire statement, Python selects the Grannie statement.
# This is because, 1. The Grannie statement was placed above the vampire statement, and 2. 3000 is greater than 100.

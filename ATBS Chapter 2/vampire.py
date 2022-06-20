# vampire.py

name = 'Alice'
age = 11
# The terminal will give you different elif messages if the 'age' value is changed
if name == 'Alice':  # If name == 'Alice', all the elif statements are skipped
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

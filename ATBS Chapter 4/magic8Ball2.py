# Magic 8 Ball With Lists (magic8ball2.py)
print()
print('magic8ball.py:')
print()


import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy and try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])
# This expression selects a random number from 0-9 (the length of the list), then subtracts 1 from it.

print(len(messages))

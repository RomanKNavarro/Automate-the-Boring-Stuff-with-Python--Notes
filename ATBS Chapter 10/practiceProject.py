import random
guess = ''
while guess not in ('heads', 'tails'):
   print('Guess the coin toss! Enter heads or tails:')
   guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
   print('You got it')
else:
   print('Nope! Guess again!')
   guess = input()
   if toss == guess:
      print('You got it!')
   else:
      print('Nope. You are really bad at this game.')


# The problem with this program is that the 'else' print statement will always return no matter what,
# since 'toss == guess' will always return False. This is because 'guess' can be either 'heads' or
# 'tails', and 'toss' can be either 1 and 0.


# fixed version

import random
guess = ''
while guess not in ('heads', 'tails'):
   print('Guess the coin toss! Enter heads or tails:')
   guess = input() 
if guess == random.choice(['heads', 'tails']):
   print('You got it')
else:
   print('Nope! Guess again!')
   guess = input()
   if guess == random.choice(['heads', 'tails']):
      print('You got it!')
   else:
      print('Nope. You are really bad at this game.')

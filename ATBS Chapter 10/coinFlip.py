import random
heads = 0
for i in range(1, 1001):
   if random.randint(0, 1) == 1:    
      heads = heads + 1             
   if i == 500: 
      print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')

# 0 represents tails and 1 represents heads. For 1000 times, the random.randint() function
# chooses either 1 or 0. Everytime '1' is chosen, the value of 'heads' increments by 1. When
# the loop has finished, the total amount of times heads was chosen is printed. When using the
# Debugger, instead of having to click 'Over' thousands of times to iterate through the entire
# loop, a 'breakpoint' can be set instead, so when 'Go' is pressed, the program will pause where
# the breakpoint is set. Here, the breakpoint is set on the half-way point, so the program will
# pause on the 500th iteration. The current value of 'heads' can be seen in the 'Globals' category
# up to this point.

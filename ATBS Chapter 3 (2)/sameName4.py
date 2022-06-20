# sameName4.py
print()
print('sameName4.py:')
print()

def spam():
     #print(eggs)      # The value of 'eggs' was placed after the print statement, instead of before, so it will not print 'spam local'.
     eggs = 'global'  # It will neither print the global statement, so therefore it will display an error message.


eggs = 'global'
spam()

# sameName2.py
print()
print('sameName2.py:')
print()


def spam():
    global eggs     # The 'global' function is used to modify a global variable from the safety of a function.
    eggs = 'spam'


eggs = 'global'    # Here, the global variable, 'eggs' was set to 'global'. But then 'eggs' was made into a global variable from within the spam() function.
spam()             # So now spam() controls the value of 'eggs', which was set to 'spam'. Due to this, 'eggs' will print as 'spam' instead of 'global'.
print(eggs)

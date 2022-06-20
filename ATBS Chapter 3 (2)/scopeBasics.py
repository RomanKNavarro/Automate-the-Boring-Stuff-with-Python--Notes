# The basics of Scopes



# Local Variables Cannot Use Variables in Other Local Scopes
print()
print('Local Variables Cannot Use Variables in Other Local Scopes:')
print()


def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
bacon()
# Since the functions spam() and bacon() both have their own local scope, the variables in them cannot be used in the global scope, nor can they be used
# in other local scopes. Here, both functions are using the variable 'eggs'. In spam(), eggs = 99, and in bacon(), eggs = 0. Python explicitly prints the
# value from spam(), because, while it was defined, just as bacon(), bacon() was not called, and spam() was. Even then, if bacon() was called, it's 'eggs'
# value will still not print because 'def bacon()' lacks the 'print(eggs)' statement, unlike spam().
# guessTheNumber.py (modded)



# Global Variables can be read from a Local Scope
print()
print('Global Variables Can Be Read from a Local Scope:')
print()

def spam():
    print(eggs)     # 'eggs', which is a global variable, is being printed from a local print statement in spam()
eggs = 42
spam()
print(eggs)



# Local and Global Variables with the Same Name (sameName.py)
print()
print('Local and Global Variables with the Same Name (sameName.py):')
print()

def spam():
     eggs = 'spam local'
     print(eggs)

def bacon():
      eggs = 'bacon local'
      print(eggs)   # prints 'bacon local'
      spam()   # prints 'spam local'
      print(eggs)   #prints 'bacon local'

eggs = 'global'
bacon() # again, prints 'bacon local', 'spam local', and 'bacon local
print(eggs)    #prints 'global'
# While using different variables with the same name is legal in Python, it's best not to, as this can cause confusion

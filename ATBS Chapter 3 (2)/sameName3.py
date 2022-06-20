# sameName3.py
print()
print('sameName.py:')
print()


def spam():
    global eggs
    eggs = 'spam'  # this is a global variable


def bacon():
    eggs = 'bacon'  # this is a local variable


def ham():
    print(eggs)  # this is a global variable


eggs = 42  # this is a global variable
spam()
print(eggs)

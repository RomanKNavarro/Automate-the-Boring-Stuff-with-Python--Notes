# The copy Module's copy() and deepcopy()
# copy() is used to create a duplicate of a list, but with a different ID number. Because of this, any changes made to the duplicate list will not affect the original list.
# deepcopy() does the same as copy() but is used for lists that contain other lists.



import copy
spam = ['a','b','c','d']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

fooden = [['bratwurst', 'knockwurst', 'blutwrust'],['schokolade', 'pumpernickel', 'schwarzbrot']]
Hamburgen = copy.deepcopy(fooden)
Hamburgen[0][2] = 'currywurst'
print(fooden)
Hamburgen

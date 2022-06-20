# Lists have what are called 'references'. When a list is assigned to a variable, it is actually the list's reference that is assigned to the variable, and not the list itself. If the variable were to be assigned to another variable, then the reference would be transfered over, and now both variables would be referencing the same list. This means that if one variable is modified, the other will be too.



spam = 42
cheese = spam
spam = 100

print(cheese)
print(spam)

# when 'spam' was assigned to 'cheese', it had the value 42. When 'spam' was changed to 100, this did not affect the 'cheese' variable, and it remained with 42.



spam = [0, 1, 2, 3, 4, 5]
cheese = spam

cheese[0] = "I'm"
spam[1] = "The"
cheese[2] = "Greatest"
spam[3] = 'Of'
cheese[4] = 'All'
spam[5] = 'Time'

print(spam)
print(cheese)

# This is not the case with lists, however. When cheese[1] changed from '1' to 'Hello!', it happened to spam[1] as well. This is because of the reference that was assigned to the variables.
# In this case, the reference assigned to 'spam' when the list was first created was copied over to 'cheese' in the second line. Because of this, both 'spam' and 'cheese' now refer to the same list,
# and if one of themis modified, the other one will be modified as well. References work with 'Dictionaries' as well, which will be explained later on.

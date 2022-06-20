# Self Lecture On Scopes:
print('Self Lecture On Scopes:')
print()
# In Python, there are Global Variables and Local Variables. Each exist respectively in the Global Scope and the Local Scope. Variables that exist in the
# Global Scope are assigned outside of any functions, while variables and other parameters assigned in functions exist inside of the Local Scope. Keep in
# mind that each function has it's own Local Scope. So while there can be multiple Local Scopes in a program, there only exists one Global Scope.

def local():
     lscopes = 5
     print('While there can be ' + str(lscopes)  + ' Local Scopes in a program,')

local()
# Everything inside of this function exists in it's local scope ^^^

gscopes = '1'
print('There is only ' + gscopes + ' Global Scope.')
# The variable 'gscopes' and the print statement exist in the Global Scope, as they are not assigned
# in any functions, like local()

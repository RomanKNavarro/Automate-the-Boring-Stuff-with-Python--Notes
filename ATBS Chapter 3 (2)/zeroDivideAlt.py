# zeroDivide.py alternative
print()
print('alternative:')
print()

def spam(divideBy):
     return 42 / divideBy

try:                                         # Using 'try' and 'except' statements in function calls also catches any potential errors.
     print(spam(2))
     print(spam(12))
     print(spam(0))
     print(spam(1))                          # print(spam(1)) does not appear because once the 'except' clause has been called,
                                             # the code does not return to the 'try' clause.
except ZeroDivisionError:
     print('Error: Invaild argument')


# End of Chapter Practice Project (The Collatz Sequence)
print()
print('The Collatz Sequence:')
print()

def collatz(number):
    if number % 2 == 0:
         print(number // 2)
    if number % 2 == 1:
         print(3 * number + 1)

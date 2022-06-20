# zeroDivide.py
print()
print('zeroDivide.py:')
print()

def spam(divideBy):                          # without the 'try' and 'except' statements, the program will display the 'ZeroDivisionError' error message.
    try:                                     # 'ZeroDivisionError' is an error that python displays whenever a number is divided by zero.
        return 42 / divideBy                 # The 'try' statement contains the code that causes the error.
    except ZeroDivisionError:                # The 'except' statement contains the error and what to do with it, rather than having the program crash.
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

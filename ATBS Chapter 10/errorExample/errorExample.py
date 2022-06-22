def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message.')

spam()

# Whenever an error is detected, a 'traceback' is returned in the Shell. The traceback
# contains the sequence of function calls that led to the error, the line number of
# each function call, and the error message itself. The sequence of function calls is
# called the 'call stack'. The last function call in the call stack is where the error
# itself actually occured. The traceback is returned whenever a raised exception is
# unhandled, as shown in the above example.

# When this program is ran, the traceback returned shows that the error in this program
# is the unhandled raised exception, and displays the exception's message. This error occured
# on line 5 in bacon(), and the call to bacon() occured on line 2, in spam(), which it itself
# was called on line 7.





def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')    
    if width <= 2:
        raise Exception('Width must be geater than 2.')                 
    if height <= 2:
        raise Exception('Height must be greater than 2.')               

# The first raised exception is that the first argument (symbol) must be a single character,
# The second one is that the second argument (width) must be 2 or more, and the third raised
# exception is that the third argument (height) must be 2 or more as well. Once an Exception
# is detected, an Exception Object is returned.

    print(symbol * width)                           
    for i in range(height -2):
        print(symbol + (' ' * (width -2)) + symbol)  
    print(symbol * width)                           

# The first print statement prints out the top row of the square. The for loop
# subtracts 2 from 'height' so that the square isn't 2 rows higher. Inside
# the loop, the 'height' number determines the amount of rows that will be created
# underneath the top row, minus 2. These rows consist of one symbol to the left,
# followed by spaces whose amount are determined by 'width', minus 2 (to eliminate
# 2 extra spaces in the rows), then another symbol after the spaces. The print
# statement outside the loop prints the bottom row of the square.


for sym, w, h in (('*', 4, 4), ('$', 3, 3), ('K', 30, 20), ('&', 2, 5)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exeption happened: ' + str(err))
    

# The ‘try’ statement contains the code with the anticipated exception, and the ‘except Exception as err’
# statement contains the code to execute if an Exception Object is returned by the raised exceptions, where
# the ‘err’ variable contains the Exception Object. When defining functions, the raised exceptions should always be
# located inside the function, and the ‘try’ and ‘except’ statements outside, with the function call within
# the ‘try’ statement. This is because functions do not know how to handle exceptions, typically.


# If a program contains 'raise' statements to raise exceptions but contains no 'try' and 'except' statements to
# handle the exceptions, once any of the raised exceptions are detected, the program crashes and displays the
# exception's error message.

# Since the raised exception will return an error if not handled, it is put in a 'try' clause. In the except clause, file named errorInfo.txt is created
# , where a string version of the traceback is written, using the 'traceback.format_exc()' function. Instead of having an error returned, the except
#statement makes sure to print a string stating that the traceback has been written to the file.

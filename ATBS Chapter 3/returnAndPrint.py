def retSquare(num):
    num = num *num
    return num

def printSquare(num):
    num = num * num
    print(num)

# Both of these functions, for example, when passed '4' in the shell, will return 16.
# However, printSquare() doesn't actually return 16, it simply prints the value on-screen.

# For example, if the retSquare() function is given 4 and passed to a variable named X, the return
# value of the function is what gets passed to X. Therefore, when X is called, it will return 16.

# This is not the case with printSquare(). If this function is given 4 and is passed to a variable
# named Y, 16 will automatically print, without first calling Y. If Y is called, nothing is
# returned. This is because the return value of printSquare() is None.

# This can be shown by using the 'type()' function on these variables. When used on X, it will return
# 'int', since the return value is an integer. When used on Y, on the other hand, 'NoneType' is
# returned, since it does not contain an actual return value. Because of this, X can be used with other
# values.

# If X were added with 5, 21 will be returned, since 5 too, is another integer. Y, on the other hand,
# when added with 5, will return "TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'",
# meaning that Y, being a NoneType value, cannot be added with 5, an integer value.




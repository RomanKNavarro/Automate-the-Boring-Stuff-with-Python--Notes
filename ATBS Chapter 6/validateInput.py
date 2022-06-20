# This program utilizes the .isdecimal() and is alnum() methods

while True:
    print('enter your age.')
    age = input()
    if age.isdecimal():
        break                                       # the loop will break if age is an integer
    print('Please enter a number for yout age.')    # or will print this if it is not

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break                                       # the loop will break if password contains only numbers/letters
    print('Passwords can only have letters and numbers.')
    

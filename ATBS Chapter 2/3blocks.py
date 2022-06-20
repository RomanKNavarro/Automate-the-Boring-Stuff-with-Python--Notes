# Understanding Blocks:
# Blocks begin when the indentation increases and end when it decreases
# Blocks can contain other blocks, like an if statement within an if statement

spam = 1                    
if spam == 1:                      
    print('eggs')                   # block 1
    if spam > 5:
        print('bacon')              # block 2
    else:                           
        print('ham')                # block 3
    print('niggers')                # part of block 2
print('spam')                       

#! python3

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i                                                
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

        # In order to fix the bug from the previous program, range() is given 2 arguments,
        # so as to specify where to start the loop and where to stop. The first argument
        # is '1', so that the factorial process begins at 1, and not 0. The second arguemt
        # is again 'n + 1', so that the factorial process ends at the number after 'n'. This
        # is done so that 'n' itself is included in the factorial process.
        
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(3))
logging.debug('End of program')

# When debugging programs, log messages should be used instead of print() statements because once the print
# statements are no longer needed for debugging, they have to be either commented out or deleted, which can
# take a while. If they are being deleted, print statements in the program that aren't meant for debugging
# can be accidently deleted as well. For log messages on the other hand, once they are no longer needed, the
# 'logging.disable(logging.CRITICAL)' call can be used, which will disable all of the log messages in the
# program. The only time print() statements should be used for debugging is for displaying user-friendly error
# messages in the shell.

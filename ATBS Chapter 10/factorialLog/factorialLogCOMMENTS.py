#! python3

import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# The functions within the 'logging' module are used to display 'log messages' on screen as the
# program runs. Whenever an event in the program is logged, a 'LogRecord' Object is created on
# behalf of that event. If a log message does not display, then part of the program was not executed.
# The 'basicConfig()' function determines which information from the LogRecord Object to display, as
# well as which of the five 'logging levels' to use. The first argument determines which logging level
# to use, followed by the format of the message itself, which contains the information that will be
# displayed on-screen.

# Here, the logging level used is the DEBUG level, which is the lowest of the five levels and is used typically
# for mentioning small details and diagnosing problems. The log message in 'format' is composed of the time in which
# the log message was displayed (asctime), the name of the logging level being used (levelname), and the message
# of the event (message). A log message is displayed for each 'logging.debug()' function found in the program,
# which return LogRecord Objects. The string found in these functions is the message used in the log message.

logging.debug('Start of program')                               # The first LogRecord Object indicates the start of the program   

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))             # The second indicates the start of the function
    total = 1
    for i in range(n + 1):                                           
        total *= i

        # The for loop in the function adds 1 to n so that the sequence of numbers being multiplied will be
        # 1, 2, 3, 4, 5; and not 0, 1, 2, 3, 4. However, the logging.debug() function in the for loop, which
        # tracks the iteration of i and the current value of total, reports that 0 was  included in the factorial
        # process, so the sequence was instead 0, 1, 2, 3, 4, 5. Because of this, all of the numbers get multiplied
        # by 0, resulting in the factorial of 5 (total) returning 0.
        
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

        # The third LogRecord Object, which is repeated depending on how
        # big the argument number is, tracks the current number in 'i',
        # as well as the corresponding value of 'total'.
        
    logging.debug('End of factorial(%s%%)' % (n))   # The fourth LogRecord Object marks the end of the factorial process
    
    return total

print(factorial(5))
logging.debug('End of program')

# After the factorial number is printed on-screen,the fifth
# and final LogRecord Object marks the end of the program






theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':        # The coordinates for the board
            ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])             # The board itself, which takes the keys from the 'theBoard' dictionary.
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + ', Move on which space?')
    move = input()
    theBoard[move] = turn       # This inserts X or O on the board
    print(theBoard)
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printBoard(theBoard)



# magic8Ball.py
print('magic8ball.py:')
print()


def getAnswer(answerNumber):  # getAnswer() is given the parameter, answserNumber
    if answerNumber == 1:
        return 'it is certain'  # The value in a return statement is what the expression will evaluate to
    if answerNumber == 2:
        return 'it is decided so'
    elif answerNumber == 3:  # Remember, elif statements are conditions that are checked off only when the 'if' statement is false
        return 'Yes'        # In this case, if answerNumber() is not 1, the elifs will return instead. Keep in mind that 'if' statements will also work in this example.
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)  # prints a random number 1-9

# The 3 lines above can be arranged into a single line
print(getAnswer(random.randint(1, 9)))

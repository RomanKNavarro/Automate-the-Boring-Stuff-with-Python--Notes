# guessTheNumber.py (modded)
print()
print('guessTheNumber.py (modded):')
print()

# This is a guess the number game.
possibleanswers = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20)
secretNumber = random.choice(possibleanswers)
# The program generates a random number, which is not revealed until the player either guesses it correctly, or runs out of chances to guess it.

print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())  # Gives the player 6 chances to guess the number that has been generated

    if guess not in possibleanswers:  # added third condition for numbers typed not 1-20
        print('please type a valid number')
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # the program breaks once the player runs out of guesses, or has guessed the number correctly


if guess == secretNumber:
    print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number that I was looking for was ' + str(secretNumber))

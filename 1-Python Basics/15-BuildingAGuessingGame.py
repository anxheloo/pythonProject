#Building a guessing game

secretWord = "giraffe"
guess = ""
numberOfGuesses = 0
guessLimit = 3


while guess != secretWord and numberOfGuesses < guessLimit:
    guess = input("Enter a guess: ")
    numberOfGuesses += 1

if numberOfGuesses <= guessLimit and guess == secretWord:
    print("You win!")
else:
    print("You loose!")
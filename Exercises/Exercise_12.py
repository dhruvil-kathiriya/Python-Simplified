### Guess a number between 1 - 20

import random
ran = random.randint(1,20)
guess = 0

while guess != ran:
    guess = int(input('Guess the Number : '))
    if guess < ran:
        print("It is Lesser Number")
    elif guess > ran:
        print("It is Greater Number")
    else: 
        print("Correct! You Guesed it right!!!")
    
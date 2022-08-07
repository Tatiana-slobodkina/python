import random

tries = 0

number = random.randint(1, 50)

print('Try to guess what number between 1 and 50')

while tries < 6:
    guess = int(input('Take a guess: '))

    tries += 1

    if guess < number:
        print('It is too low')
    if guess > number:
        print('It is too high')
    if guess == number:
        print(f'You guessed number in {tries} guesses')
    if guess != number and tries == 6:
        print(f"You didn't guess. The number was {number}")

# Project 12 - Guess the Number
# Ascci art - http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

import random
from day_012.art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {comp_guessed_num}")

comp_guessed_num = random.randint(1, 100)


def game_lives():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == 'hard':
        return 5
    else:
        return 10


lives = game_lives()

for life in range(lives):
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = float(input("Make a guess: "))

    if user_guess < comp_guessed_num:
        print("Too low")
    elif user_guess > comp_guessed_num:
        print("Too high.")
    elif user_guess == comp_guessed_num:
        print(f"You got it !!! The answer is {comp_guessed_num}.")
        break
    else:
        print("Wrong guess.")

    if lives > 1:
        print("Guess again.")
    lives -= 1
else:
    print("You've ran out of guessses. You lose.")


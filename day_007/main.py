# Project 7 - Hangman

import random

import pyautogui

from day_007.hangman_words import word_list
import day_007.art as art


print(art.logo)
end_of_game = False
lives = 6
random_number = random.randint(0, len(word_list) - 1)
comp_chosen_word = word_list[random_number]

display = []

for letter in comp_chosen_word:
    display.append('_')

while not end_of_game:
    user_guessed_letter = input("Guess a letter : ").lower()
    # To clear the window in pycharm
    pyautogui.hotkey('shift', 'c')

    if user_guessed_letter in display:
        print(f"You've already guessed {user_guessed_letter}")

    num = 0
    for letter in comp_chosen_word:
        if user_guessed_letter == letter:
            display[num] = letter
        num += 1

    print(' '.join(display))

    if user_guessed_letter not in display:
        lives -= 1
        print(f"You guessed {user_guessed_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose :(")
            print(f"The word is {comp_chosen_word}")

    if "_" not in display:
        if lives != 0:
            end_of_game = True
            print("You Win :)")

    print(art.stages[lives])

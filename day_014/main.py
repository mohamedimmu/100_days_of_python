# Project 14 - Higher or Lower game
# Guess who has more instagram follower
# Trail game link - http://www.higherlowergame.com/

import random
import operator as op
import pyautogui
from day_014.art import logo, vs
from day_014.game_data import data


def info(person):
    """Pass the person dict and it returns the info of the person in tuple"""
    name = person["name"]
    follower_count = person["follower_count"]
    description = person["description"]
    country = person["country"]
    return name, follower_count, description, country


def result(operator, a, b):
    return operator(a, b)


def higher_lower():
    # initialize the score and index
    score = 0
    compare_index = 0
    against_index = 1
    game_over = False
    person_info_list = random.sample(data, len(data))

    while not game_over:
        print(logo)

        compare_person_info = person_info_list[compare_index]
        compare_person_info = info(compare_person_info)
        print(f"Compare A: {compare_person_info[0]}, a {compare_person_info[2]}, from {compare_person_info[3]}.")

        print(vs)

        against_person_info = person_info_list[against_index]
        against_person_info = info(against_person_info)
        print(f"Against B: {against_person_info[0]}, a {against_person_info[2]}, from {against_person_info[3]}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A':
            operation = op.gt
        else:
            operation = op.lt

        result_status = result(operation, compare_person_info[1], against_person_info[1])

        pyautogui.hotkey("shift", "c")

        if result_status:
            score += 1
            compare_index += 1
            against_index += 1
            print(f"You're right! Current score: {score}.")

            if against_index >= len(data):
                against_index -= 50
            elif compare_index >= len(data):
                person_info_list.clear()
                person_info_list = random.sample(data, len(data))
                compare_index = 0
                against_index = 1

        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


higher_lower()

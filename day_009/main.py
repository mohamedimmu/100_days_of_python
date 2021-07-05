# Project 9 - Secret auction

import pyautogui
from day_009.art import logo

print("\nSecret auction")
print(logo)
quit_the_app = False

bider_list = []

while not quit_the_app:
    bider_name = input("What is your name? ")
    bider_price = int(input("What is your bid? ₹"))
    status_of_auction = input("Are there any other bidders? Type 'yes or 'no'\n").lower()
    # To clear the screen
    pyautogui.hotkey('shift', 'c')

    bider_details = {
        "name": bider_name,
        "bid": bider_price
    }

    bider_list.append(bider_details)

    if status_of_auction == "yes":
        continue
    elif status_of_auction == "no":
        quit_the_app = True
        highest_bid = 0
        highest_bider = ""
        for bider in bider_list:
            if bider["bid"] > highest_bid:
                highest_bid = bider["bid"]
                highest_bider = bider["name"]

        print(logo)
        print(f"The winner is {highest_bider.title()} with a bid of ₹{highest_bid}")

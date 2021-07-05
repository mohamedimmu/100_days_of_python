# Project 10 - Simple Calculator

import pyautogui
from day_010.art import logo

print(logo)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


quit_the_app = False

operation_dict = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}


def calculator():
    first_number = float(input("What's the first number?: "))
    print("+ \n- \n* \n/ \n")
    should_continue = True

    while should_continue:
        operation_key = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = operation_dict[operation_key](first_number, next_number)

        print(f"{first_number} {operation_key} {next_number} = {result}")

        status = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'q' to "
                       f"quit the app: ").lower()

        if status == "y":
            first_number = result
        elif status == "q":
            global quit_the_app
            should_continue = False
            quit_the_app = True
        else:
            should_continue = False
            pyautogui.hotkey("shift", "c")


while not quit_the_app:
    calculator()
print("\nShutting  down........")

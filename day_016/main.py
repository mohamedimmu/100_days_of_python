# Project 16 - Coffee Machine Project in OOP's

from day_016.menu import Menu
from day_016.coffee_maker import CoffeeMaker
from day_016.money_machine import MoneyMachine
  

print("\nCoffee Machine Project in OOP's\n")
coffee_machine_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while coffee_machine_on:

    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()

    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif user_choice == 'off':
        coffee_machine_on = False
        print("Coffee-Machine is shutting down......")

    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

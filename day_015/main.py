# Project 15 - Coffee machine

from day_015.menu_data import MENU, resources

money = 0


def report():
    for resource in resources:
        item = resource.title() + ": " + str(resources[resource])
        if resource == "coffee":
            item += "g"
        else:
            item += "ml"
        print(item)
    print(f"Money: ${money:.2f}")


def stock_check(coffee_ingredients):
    count = 0
    for resource in resources.values():
        if resource < coffee_ingredients[count]:
            print(f"Sorry there is not enough {resource}.")
            return False
        count += 1
    return True


def coffee(coffee_name):
    coffee_powder = MENU[coffee_name]["ingredients"]["coffee"]
    water = MENU[coffee_name]["ingredients"]["water"]
    if coffee_name == "espresso":
        milk = 0
    else:
        milk = MENU[coffee_name]["ingredients"]["milk"]

    coffee_ingredients = [water, milk, coffee_powder]

    stock = stock_check(coffee_ingredients)

    if stock:
        resources["coffee"] -= coffee_powder
        resources["water"] -= water
        resources["milk"] -= milk

        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        totat_amount = (0.01 * pennies) + (0.10 * nickles) + (0.05 * dimes) + (0.25 * quarters)
        coffee_amount = MENU[coffee_name]["cost"]

        if totat_amount > coffee_amount:
            change_amont = totat_amount - coffee_amount
            print(f"Here is ${change_amont:.2f} in change.")
        elif totat_amount < coffee_amount:
            print("Sorry that's not enough money. Money refunded.")
            return 0

        print(f"Here is your {coffee_name} ☕. Enjoy!")
        return coffee_amount


machine_status = 'ON'
while machine_status == "ON":
    print()
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        money += coffee(user_input)
    elif user_input == "off":
        print("Machine is turning off.")
        machine_status = "OFF"
    else:
        print("Something went wrong")

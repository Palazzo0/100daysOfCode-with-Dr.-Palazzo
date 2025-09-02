MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: print your welcome message, menu, and instructions.

print("WELCOME TO DR. PALAZZO'S COFFEE MACHINE!")
print("Coins Available:\n"
      "quarters = $0.25 \ndimes = $0.10 \nnickles = $0.05 \npennies = $0.01 "
      )
print("MENU:\n"
      "Espresso: $1.5\n"
      "Latte: $2.5\n"
      "Cappuccino: $3.0")
print("INSTRUCTIONS:\n"
      "Type 'off' to shut down the machine.\n"
      "Type 'Report' to know the amount of resources available for your order.\n")

#TODO 2: check for sufficient resources to make order as well as calculate the total amount of coins added and provide change
profit = 0
def check_sufficiency(order):
    order_recipe = MENU[order]["ingredients"]
    cost_for_order = MENU[order]["cost"]
    for ingredient in order_recipe:
        if order_recipe[ingredient] > resources.get(ingredient, 0):
            print(f"Sorry, there isn't enough {ingredient}.")
            return  False
        else:
            print("Please insert coin(check the top of the screen for the available coins and their values):")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            total_money_input = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if total_money_input >= cost_for_order:
                change = total_money_input - cost_for_order
                global profit
                profit += cost_for_order
                for i in order_recipe:
                    resources[i] -= order_recipe[i]
                    print(f"Here is your {order}☕. And a change of ${change:.0f}.")
                    return True
                else:
                    print("Sorry, that's not enough money. money refunded.")
                    return False
    return True

#TODO 3: assign the resources to variables for easy reference and printing
def current_resources():
    water_resource = resources["water"]
    milk_resource = resources["milk"]
    coffee_resource = resources["coffee"]
    return f"Current Resources: \nWater: {water_resource}ml \nMilk: {milk_resource}ml \nCoffee: {coffee_resource}g \nMoney: ${profit}"



user_choice_in_progress = True
while user_choice_in_progress:
    user_choice =input("What would you like? (espresso/latte/cappuccino). Check the top for the cost of each:").lower()

# TODO 5: Print Report - a report should be generated that shows  the current resource values.
    if user_choice == "report":
        print(current_resources())

# TODO 6: Turn your machine off when the user input says "off"
    elif user_choice =="off":
        print("Shutting down complete!")
        user_choice_in_progress = False
    # TODO 4:Check the user’s input to decide what to do next and the prompt should show every time action has completed.
    else:
        check_sufficiency(user_choice)
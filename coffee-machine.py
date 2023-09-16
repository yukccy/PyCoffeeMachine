from art import logo

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
    "water": 3000,
    "milk": 3000,
    "coffee": 1000,
    "money": 0
}

def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def calc_coins(num_quarters, num_dimes, num_nickels, num_pennies, product):
    total_value_quarters = float(num_quarters) * 0.25
    total_value_dimes = float(num_dimes) * 0.1
    total_value_nickels = float(num_nickels) * 0.05
    total_value_pennies = float(num_pennies) * 0.01
    total_value = total_value_quarters + total_value_dimes + total_value_nickels + total_value_pennies
    changes = total_value - MENU[product]["cost"]
    return round(changes,2)

def check_resources(product):
    for item in MENU[product]["ingredients"]:
        continue_flag = False
        if MENU[product]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            break
        else:
            continue_flag = True
    return continue_flag

def update_resources(product):
    for item in MENU[product]["ingredients"]:
        resources[item] = resources[item] - MENU[product]["ingredients"][item]
    resources["money"] = resources["money"] + MENU[product]["cost"]

order_flag = True

while order_flag:
    print(logo)
    action = input("What would you like? (espresso/latte/cappuccino) ")
    if action == "report":
        report()
        order = input("Want to order? (yes/no) ")
        if order == "no":
            order_flag = False
    else:
        continue_flag = check_resources(product=action)
        if continue_flag == True:
            print("Please insert coins.")
            num_quarters = input("How many quarters? ")
            num_dimes = input("How many dimes? ")
            num_nickels = input("How many nickels? ")
            num_pennies = input("How many pennies? ")
            changes = calc_coins(num_quarters=num_quarters, num_dimes=num_dimes, num_nickels=num_nickels, num_pennies=num_pennies, product=action)
            if changes < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                update_resources(product=action)
                print(f"Here is ${changes} in change.")
                print(f"Here is your {action}. Enjoy!")
                order = input("Want to order again? (yes/no) ")
                if order == "no":
                    order_flag = False
                    print("Bye!")
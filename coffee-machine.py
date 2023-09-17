from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

order_flag = True
while order_flag:
    print(logo)
    all_items = menu.get_items()
    choice = input(f"What would you like? {all_items} ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        order = input("Want to order? (yes/no) ")
        if order == "no":
            order_flag = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        order = input("Want to order again? (yes/no) ")
        if order == "no":
            order_flag = False
            print("Bye!")
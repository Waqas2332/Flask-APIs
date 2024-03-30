from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()

while True:
    choice = input(f"What would you like? ({menu.get_items}): ")
    if choice == "off":
        break
    elif choice == "report":
        coffee.report()
        money.report();
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
    
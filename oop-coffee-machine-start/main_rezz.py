
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
print(coffee_maker.report())
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_item = MenuItem

menu.get_items()


is_on = True
while is_on:
    choice = input("What you want: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
        is_on = False

    drink = menu.find_drink(choice)

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            continue

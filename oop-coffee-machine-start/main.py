from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


rez_coffee_machine = CoffeeMaker()
rez_money_machine = MoneyMachine()

while True:
    your_drink = input('what you wanttttt!!!\n: ')
    if your_drink == 'off':
        break
    if your_drink == 'report':
        rez_money_machine.report()
        continue

    drink_name = Menu().find_drink(your_drink)

    if drink_name is not None:
        if rez_coffee_machine.is_resource_sufficient(drink_name):
            if rez_money_machine.make_payment(drink_name.cost):
                rez_coffee_machine.make_coffee(drink_name)
                rez_coffee_machine.report()









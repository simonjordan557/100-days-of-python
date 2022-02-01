from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    customer_request = input(f"What would you like? {menu.get_items()}").lower()
    drink_ordered = menu.find_drink(customer_request)
    if customer_request == "report":
        coffee_maker.report()
        continue
    elif customer_request == "off":
        print("Switching off...")
        sys.exit()
    elif drink_ordered is None:
        continue
    else:
        if not coffee_maker.is_resource_sufficient(drink_ordered):
            continue
        else:
            if not money_machine.make_payment(drink_ordered.cost):
                continue
            else:
                coffee_maker.make_coffee(drink_ordered)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu_item = MenuItem()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


conti = True
while conti:
    options = menu.get_items()
    prompt = input(f"What would you like? ({options}): ")

    if prompt == "report":
        coffee_maker.report()
        money_machine.report()

    elif prompt == "off":
        conti = False

    else:
        drink = menu.find_drink(prompt)
        enough = coffee_maker.is_resource_sufficient(drink)
        if enough:
            cost = drink.cost
            payment = money_machine.make_payment(cost)
            if payment:
                coffee_maker.make_coffee(drink)

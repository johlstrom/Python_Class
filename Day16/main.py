from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_menu = Menu()
coffee_maker = CoffeeMaker() 
machine_on = True



while machine_on:
    options = coffee_menu.get_items()
    user_choice = input(f"What would you like? {options}:")

    match user_choice:
        case "off":
            machine_on = False
        case "report":
            coffee_maker.report()
            money_machine.report()            
        case _:
            drink = coffee_menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            
""" OOP Coffee Machine Project Code """

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

clear()

print('                                 COFFEE MACHINE                                 ')
print('--------------------------------------------------------------------------------')
print('Choose an option: \n- O to Order \n- R to Report \n- S to Shut Down')
option = input('What would you like? --> ').upper()

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while option != 'S':
    if option == 'R':
        coffee_maker.report()
        money_machine.report()
    elif option == 'O':
        order = input(f'What would you like to order? {menu.get_items()} --> ').lower()
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print('  Invalid Option, Try Again')
    print('\nChoose an option: \n O to Order \n R to Report \n S to Shut Down')
    option = input('What would you like? --> ').upper()

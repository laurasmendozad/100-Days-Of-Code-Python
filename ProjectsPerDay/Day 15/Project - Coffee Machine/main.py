""" Coffee Machine Project Code """
from data import MENU,resources,units
from replit import clear

clear()
print('                                 COFFEE MACHINE                                 ')
print('--------------------------------------------------------------------------------')
print('Choose an option: \n - O to Order \n - R to Report \n - S to Shut Down')
option = input('What would you like? --> ').upper()
coffees = list(MENU.keys())
while option != 'S':
    OUT = False
    if option == 'R':
        for r in resources.items():
            print(f"   {r[0].capitalize()}: {r[1]} {units[r[0]]}")
    elif option == 'O':
        print('   Menu:')
        for o in MENU.items():
            print(f"   * {o[0].capitalize()}")
        order = input('   What would you like to order? --> ').lower()
        if order not in coffees:
            print('     Not valid element')
            OUT = True
        if OUT is not True:
            for i in MENU[order]['ingredients'].items():
                if i[1] > resources[i[0]]:
                    print(f'    Sorry there is not enough {i[0]}')
                    OUT = True
                else:
                    resources[i[0]] -= i[1]
        if OUT is not True:
            print('     Please Insert Coins')
            quarters = int(input('     + How many quarters? --> '))
            dimes = int(input('     + How many dimes? --> '))
            nickles = int(input('     + How many nickles? --> '))
            pennies = int(input('     + How many penniess? --> '))
            payment = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
            if payment < MENU[order]['cost']:
                print("     Sorry that's not enough money. Money refunded.")
                for i in MENU[order]['ingredients'].items():
                    resources[i[0]] += i[1]
            else:
                resources['money'] += MENU[order]['cost']
                change = round(payment - MENU[order]['cost'],2)
                print(f"     Here is {change} USD in change")
                print(f"     Here is your {order} ☕. Enjoy it!")
    else:
        print('  Invalid Option, Try Again')
    print('\nChoose an option: \n O to Order \n R to Report \n S to Shut Down')
    option = input('What would you like? --> ').upper()

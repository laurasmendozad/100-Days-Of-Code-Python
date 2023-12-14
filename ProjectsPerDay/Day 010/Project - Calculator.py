from art import logo
from replit import clear

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {'+': add,
             '-': subtract,
             '*': multiply,
             '/': divide}
def calculator():
    c = 'y'
    print(logo)
    print('                                              CALCULATOR                                              ')
    print('------------------------------------------------------------------------------------------------------')     
    num1 = float(input("What's the first number?: "))
    while c == 'y':
        print("The operations avaliable are the following")
        for key in operations:
            print(key,end=" ")
        symbol = input('\nType an operation from the line above: ')
        num2 = float(input("What's the next number?: "))
        operation = operations[symbol]
        result = operation(num1,num2)
        print(f'{num1} {symbol} {num2} = {result}')
        c = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit: ").lower()
        if c == 'y':
            num1 = result
        elif c == 'n':
            clear()
            calculator()
calculator()
print('------------------------------------------------------------------------------------------------------')     
    
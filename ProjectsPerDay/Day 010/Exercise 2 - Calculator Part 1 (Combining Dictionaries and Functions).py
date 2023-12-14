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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
print("The operations avaliable are the following")
for key in operations:
    print(key,end=" ")
symbol = input('\nType an operation from the line above: ')
operation = operations[symbol]
result = operation(num1,num2)
print(f'{num1} {symbol} {num2} = {result}')
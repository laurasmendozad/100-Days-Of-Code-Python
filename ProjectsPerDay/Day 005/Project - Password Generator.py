#Password Generator Project
import random

print('                              PASSWORD GENERATOR                               ')
print('-------------------------------------------------------------------------------')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password = list()
for i in range(0,nr_letters):
    password.append(random.choice(letters))
for i in range(0,nr_symbols):
    password.append(random.choice(symbols))
for i in range(0,nr_numbers):
    password.append(random.choice(numbers))

password = ''.join([str(w) for w in random.sample(password, len(password))])
print(f'\nHere is your password: {password}')

print('-------------------------------------------------------------------------------')

from art import logo
from replit import clear
from random import randint

clear()
print(logo)
print('                                                           GUESS THE NUMBER GAME                                                           ')
print('-------------------------------------------------------------------------------------------------------------------------------------------')

print("I'm thinking of a number between 1 and 100.")
n = randint(1,100)
# print(f"Psst, the correct answer is {n}")

c = input("Choice a difficulty. Type 'easy' or 'hard' --> ")

if c.lower() == 'easy':
    a = 10
elif c.lower() == 'hard':
    a = 5
else:
    print('Invalid Option')
    exit()

for i in range(0,a):
    print(f"You have {a-i} attemps remaining to guess the number.")
    g = input("Make a guess --> ")
    if int(g) < n:
        print("Too Low.")
    elif int(g) > n:
        print("Too High.")
    elif int(g) == n:
        print(f"You got it! The answer is {n}, you win :)")
        exit()

    if i < a-1:
        print("Guess again")

print(f"You've run out of guesses. The answer is {n}, you lose :(")
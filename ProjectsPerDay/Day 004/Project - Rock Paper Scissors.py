rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print('                              ROCK PAPER SCISSORS                              ')
print('-------------------------------------------------------------------------------')

y = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors --> '))
l = [rock,paper,scissors]
c = random.randint(0,len(l)-1)

if y > 3 or y < 0:
    print('The input is not supported, try again')
else:
    print('\nYour Choice')
    print(l[y])
    print("Computer's Choice")
    print(l[c])

    if c == y:
        print("GOOD LUCK :) There's a draw")
    #     paper vs scissors      scissors vs rock         rock vs paper
    elif (y == 1 and c == 2) or (y == 2 and c == 0) or (y == 0 and c == 1):
        print('BETTER LUCK NEXT TIME :/ ¡Computer is the winner!')
    #     paper vs scissors      scissors vs rock         rock vs paper
    elif (c == 1 and y == 2) or (c == 2 and y == 0) or (c == 0 and y == 1):
        print('CONGRATULATIONS :D ¡You are the winner!')
    
print('-------------------------------------------------------------------------------')

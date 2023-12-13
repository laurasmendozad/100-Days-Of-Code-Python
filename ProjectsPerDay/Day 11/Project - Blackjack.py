############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

##################### Solution #####################
from tkinter import Y
from art import logo, card_art
from replit import clear
import random

def score_calculation(cards):
    score = 0
    c = []

    for n in cards:
        score = score + cards_number[n]
        c.append(cards_art[n])

    if 0 in cards and score > 21:
        score = score - 10

    return score, c

def print_cards(u_score, u_c, c_c):
    print('User Cards',end="\t\t\t")
    print(f'User Score: {u_score}',end=" ")
    print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('  '), key=len))) for x in s.split('\n')] for s in u_c])], sep='\n')
    print('\nComputer Card',end=" ")
    print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('  '), key=len))) for x in s.split('\n')] for s in [c_c[0]]])], sep='\n')

def set_result(u_score, c_score):
    b = 0
    if ((u_score == 21) or (c_score > 21 and u_score < 21)):
        b = 1
    elif ((c_score == 21) or (c_score < 21 and u_score > 21)):
        b = 2  
    return b

def final_result(b,u_score, c_score):
    if (u_score > c_score or b == 1):
        print('You Win :)')
        print('Total User Score:',u_score)
        print('Total Computer Score:',c_score)
        print('------------------------------------------------------------------------------------------------------')

    elif (u_score < c_score or b == 2):
        print('You Lose :(')
        print('Total User Score:',u_score)
        print('Total Computer Score:',c_score)
        print('------------------------------------------------------------------------------------------------------')
        
    elif (u_score == c_score):
        print('Draw')
        print('Total User Score:',u_score)
        print('Total Computer Score:',c_score)
        print('------------------------------------------------------------------------------------------------------')
        

clear()

cards_number = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_art = {}
for i in range(0,len(card_art)):
    cards_art[i] = card_art[len(card_art)-1-i]

print(logo)
print('                                            BLACKJACK GAME                                            ')
print('------------------------------------------------------------------------------------------------------')



start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N' --> ")

while start.upper() == 'Y':
    i = 0
    u_l = list()
    c_l = list()
    r = list()
    for x in range(0,len(card_art)):
        r.append(x)
    a_c = 'Y'

    while a_c.upper() == 'Y':
        if i == 0:
            u_l.append(random.sample(range(0,len(card_art)),2))
            c_l.append(random.sample(range(0,len(card_art)),2))

            [u_score,u_c] = score_calculation(u_l[0])
            [c_score,c_c] = score_calculation(c_l[0])

        if i > 0:
            for j in range(0,len(card_art)):
                if j in u_l[0]:
                    try:
                        r.remove(j)
                    except:
                        None

            u_l.append(random.sample(r,1))
            u_l[0] = u_l[0] + u_l[1]
            del u_l[1]
            [u_score,u_c] = score_calculation(u_l[0])

            if c_score < 17:
                c_l.append(random.sample(range(0,len(card_art)),1))
                c_l[0] = c_l[0] + c_l[1]
                del c_l[1]
                [c_score,c_c] = score_calculation(c_l[0])

        print_cards(u_score, u_c, c_c)
        b = set_result(u_score, c_score)
        i += 1
        if b == 1 or b == 2:
            break
        else:
            a_c = input("Type 'Y' to get another card or 'N' to pass --> ")

    b = final_result(b, u_score, c_score)
    start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N' --> ")
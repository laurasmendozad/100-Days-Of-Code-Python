from art import logo, vs
from game_data import data
from replit import clear
import random

clear()
print(logo)
print('                                 HIGHER LOWER GAME                                 ')
print('-----------------------------------------------------------------------------------')

score = 0

def format_data(option, item):
    name = item['name']
    description = item['description']
    country = item['country']
    if description.lower().startswith('a') or description.lower().startswith('e') or description.lower().startswith('i') or description.lower().startswith('o') or description.lower().startswith('u'):
        prep = 'an'
    else:
        prep = 'a'
    print(f"{option}: {name}, {prep} {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'

game_on = True
while(game_on):
    item = {}
    item['A'] = random.choice(data)
    item['B'] = random.choice(data)
    while item['B'] == item['A']:
        item['B'] = random.choice(data)

    format_data('Compare A',item['A'])
    print(vs)
    format_data('Against B',item['B'])

    more_followers = input("Who has more followers? Type 'A' or 'B' --> ")
    result = check_answer(more_followers.upper(), item['A']['follower_count'], item['B']['follower_count'])

    clear()
    print(logo)
    if result:
        score += 1
        print(f"You're right! Current score: {score}.")        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False
        print('-----------------------------------------------------------------------------------')

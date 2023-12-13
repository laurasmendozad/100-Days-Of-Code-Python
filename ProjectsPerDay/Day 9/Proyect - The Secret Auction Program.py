from replit import clear
import operator
from art import logo

print(logo)
print('                SECRET AUCTION PROGRAM                ')
print('------------------------------------------------------')

d = {}
c = 'yes'
while c == 'yes':
    name = input("What is your name? --> ")
    bid = int(input("What is your bid? --> $"))
    d[name] = bid
    c = input("Are there any other bidders? Type 'yes' or 'no' --> ").lower()
    clear()
max_bidder = max(d.items(), key=operator.itemgetter(1))[0]
print(f'The winner is {max_bidder} with a bid of ${d[max_bidder]}')
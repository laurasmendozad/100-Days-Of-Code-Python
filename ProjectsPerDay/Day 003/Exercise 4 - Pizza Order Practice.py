# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size.upper() == 'S':
    bill = 15
    if add_pepperoni.upper() == 'Y':
        bill += 2
elif size.upper() == 'M':
    bill = 20
    if add_pepperoni.upper() == 'Y':
        bill += 3
elif size.upper() == 'L':
    bill = 25
    if add_pepperoni.upper() == 'Y':
        bill += 3

if extra_cheese.upper() == 'Y':
    bill +=1

print('Your final bill is: $' + str(bill) + '.')

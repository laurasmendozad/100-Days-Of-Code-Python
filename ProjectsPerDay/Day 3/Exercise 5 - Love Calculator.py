# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
T = name.lower().count('t')
R = name.lower().count('r')
U = name.lower().count('u')
E = name.lower().count('e')
L = name.lower().count('l')
O = name.lower().count('o')
V = name.lower().count('v')
E = name.lower().count('e')

score = int(str(T+R+U+E) + str(L+O+V+E))
if (score <= 10) or (score >= 90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif (score >= 40) and (score <= 50):
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')

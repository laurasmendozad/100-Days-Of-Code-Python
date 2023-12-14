def finish(n):
    print(f'    STEP {n}: Unreached')
    print('MISION: Incomplete')
    print('                                   GAME OVER                                   ')
    print('-------------------------------------------------------------------------------')

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('                                TREASURE ISLAND                                ')
print('-------------------------------------------------------------------------------')
print('MISION: Find the treasure')
print("    STEP 1: You're across the road. Where do you want to go?")
s1 = input("            Type 'L' if you want to turn left and 'R' if you want to turn right --> ")
if s1.upper() == 'L':
    print("    STEP 1: Reached")
    print("    STEP 2: You're come to a lake. There is an island in the middle of the lake.")
    s2 = input("            Type 'W' if you want to wait for a boat and 'S' if you want to swim across --> ")
    if s2.upper() == 'W':
        print("    STEP 2: Reached")
        print("    STEP 3: You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?.")
        s3 = input("            Type 'R' for red, 'Y' for yellow and 'B' for blue --> ")
        if s3.upper() == 'R':
            print("            :(  Oh no, It's a room full of fire, you get burned")
            finish(3)
        elif s3.upper() == 'Y':
            print('            :)  Oh yes, you found the treasure')
            print('    STEP 3: Reached')
            print('MISION: Complete')
            print('                                CONGRATULATIONS                                ')
            print('-------------------------------------------------------------------------------')       
        elif s3.upper() == 'B':
            print("            :(  Oh no, It's a room full of beasts, you get eaten by them")
            finish(3)
        else:
            finish(3)
    else:
        print('            :(  Oh no, you get attacked by an angry trout')
        finish(2)
else:
    print('            :(  Oh no, you fell into a hole')
    finish(1)

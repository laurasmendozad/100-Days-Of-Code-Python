#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {word}.')

#Create blanks
display = ['_' for w in word]

while '_' in display:
    end = False
    letter = input("Guess a letter: ").lower()

    for p in range(len(word)):
        if word[p] == letter:        
            display[p] = letter

    #TODO-2: - If guess is not a letter in the word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if letter not in word:
        lives -= 1
        if lives == 0:
            print('You lose')
            end = True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    if end is True:
        exit()

#If user has got all letters.
print("You win.")
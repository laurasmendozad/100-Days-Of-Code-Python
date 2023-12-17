#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {word}.')

#Create blanks
display = ['_' for w in word]

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while '_' in display:
    letter = input("Guess a letter: ").lower()

    #Check guessed letter
    for p in range(len(word)):
        if word[p] == letter:        
            display[p] = letter

    print(display)
print('You Win')

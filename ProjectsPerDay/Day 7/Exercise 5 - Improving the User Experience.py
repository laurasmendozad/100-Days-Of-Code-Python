#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

word = random.choice(word_list)
list_of_letters = []
end = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {word}.')

#Create blanks
display = ['_' for w in word]

while '_' in display:
    letter = input("Guess a letter: ").lower()
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if letter in list_of_letters:
        print(f"You've already guessed {letter}")
    else:
        #Check guessed letter
        for p in range(len(word)):
            if word[p] == letter:        
                display[p] = letter

        #Check if user is wrong.
        if letter not in word:
            #TODO-5: - If the letter is not in theword, print out the letter and let them know it's not in the word.
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                print('You lose.')
                end = True
    
    list_of_letters.append(letter)
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
    if end is True:
        exit()

print('You win.')
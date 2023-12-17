import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages

word = random.choice(word_list)
list_of_letters = []
end = False
lives = 6

clear()
print(logo)
# print(f'Pssst, the solution is {word}.')
display = ['_' for w in word]

while '_' in display:
    letter = input("Guess a letter: ").lower()

    clear()

    if letter in list_of_letters:
        print(f"You've already guessed {letter}")
    else:
        for p in range(len(word)):
            if word[p] == letter:
                display[p] = letter

        if letter not in word:
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                print('You lose.')
                end = True

    list_of_letters.append(letter)
    print(f"{' '.join(display)}")
    print(stages[lives])
    if end is True:
        exit()

print('You win.')

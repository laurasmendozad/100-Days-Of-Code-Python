''' NATO Alphabet Project '''
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row[0]: row[1] for (index, row) in data.iterrows()}

w = input("Enter a word: ")
w_alph = [data_dict[letter.capitalize()] for letter in w]
print(w_alph)

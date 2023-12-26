''' NATO Alphabet Project '''
import pandas as pd

data = pd.read_csv(r"ProjectsPerDay\Day 026\Project - NATO Alphabet\nato_phonetic_alphabet.csv")
data_dict = {row.iloc[0]: row.iloc[1] for (index, row) in data.iterrows()}

w = input("Enter a word: ")
w_alph = [data_dict[letter.capitalize()] for letter in w]
print(w_alph)

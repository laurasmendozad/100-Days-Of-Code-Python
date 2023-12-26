''' NATO Alphabet Project '''
import pandas as pd

data = pd.read_csv(r"ProjectsPerDay\Day 026\Project - NATO Alphabet\nato_phonetic_alphabet.csv")
data_dict = {row.iloc[0]: row.iloc[1] for (index, row) in data.iterrows()}

def generate_phonetic():
    ''' Generate Word with Phonetic Alphabet '''
    w = input("Enter a word: ")
    try:
        w_alph = [data_dict[letter.capitalize()] for letter in w]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(w_alph)

generate_phonetic()

# Project 26 - NATO Alphabet Project

import pandas as pd

print("NATO Alphabet Project")

# dataframe to dict:
df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

# Created a list of the phonetic code words from a word that the user inputs.

user_input = input('Enter a word: ').upper()

nato_phonetic_output = [nato_phonetic_alphabet[letter] for letter in user_input
                        if letter in nato_phonetic_alphabet.keys()]

print(nato_phonetic_output)

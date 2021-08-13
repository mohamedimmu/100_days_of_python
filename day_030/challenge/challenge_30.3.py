import pandas as pd

print("NATO Alphabet Project")

# dataframe to dict:
# ../  It is used to go back one step from working directory
df = pd.read_csv('../../day_026/nato_phonetic_alphabet.csv')
nato_phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

# Created a list of the phonetic code words from a word that the user inputs.

while True:
    user_input = input('Enter a word: ').upper()
    try:
        nato_phonetic_output = [nato_phonetic_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_phonetic_output)
        break

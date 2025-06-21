import pandas

data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
name = input("What's your name?: ").upper()
words_list = [data_dict[letter] for letter in name]
print(words_list)

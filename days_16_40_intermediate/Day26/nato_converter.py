import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# one way
# phonetic_dict = {data.iloc[i].letter: data.iloc[i].code for i in range(len(data))}
# print(phonetic_dict)

# Another way
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

import enchant
import pandas as pd

def is_english_word(word):
    d = enchant.Dict("en_US")
    return d.check(word)

csvfile = pd.read_csv('WordList.csv', skiprows=1)
csvWord = csvfile.sample(ignore_index=True)
print(csvWord)















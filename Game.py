import pandas as pd

csvfile = pd.read_csv('WordList.csv', skiprows=1)
csvWord = csvfile.sample(ignore_index=True)
gameWord = csvWord.to_string()
gameWord = gameWord.strip().split(" ")
gameWord = gameWord[2]
print(gameWord)

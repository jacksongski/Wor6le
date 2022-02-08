import pandas as pd

csvfile = pd.read_csv('WordList.csv', skiprows=1)
csvWord = csvfile.sample(ignore_index=True)
gameWord = csvWord.to_string()
gameWord = gameWord.strip().split(" ")
gameWord = gameWord[2]
print(gameWord) # REMOVE BEFORE GAMEPLAY
# Put random word into a length 6 array for comparisons
gameArr = []
for i in gameWord:
    gameArr.append(i)

print("Welcome to 6 Letter Word Game!\nBegin by entering a 6 letter word.")
win = False
guessWordArr = []
# Begin game sequence
while not win:
    guessWord = input()
    for i in guessWord:     # put into character array
        guessWordArr.append(i)
    if gameArr == guessWordArr:
        win = True
        break












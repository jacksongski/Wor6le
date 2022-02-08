from numpy import char
import pandas as pd

csvfile = pd.read_csv('WordList.csv', skiprows=1)
csvWord = csvfile.sample(ignore_index=True)
gameWord = csvWord.to_string()
gameWord = gameWord.strip().split(" ")
gameWord = gameWord[2]
print(gameWord) # REMOVE BEFORE GAMEPLAY
# Put random word into a length 6 array for comparisons

class Letter:
    char = ''
    status = 'red'
    word = ''
    def __init__(self,char,status,word): 
          self.char = char
          self.status = status
          self.word = word

gameArr = []
for i in gameWord:
    gameArr.append(Letter(i, 'green', gameWord))

print("Welcome to 6 Letter Word Game!\nBegin by entering a 6 letter word.")
win = False
guessWordArr = []
# Begin game sequence
while not win:
    guessWordArr.clear()
    guessWord = input("Enter: ")
    index = 0
    for i in guessWord:     # put into character array
        if not gameWord.__contains__(i):
            guessWordArr.append(Letter(i, 'red', guessWord))
        elif not gameArr[index].char == i:
            guessWordArr.append(Letter(i, 'yellow', guessWord))
        else:
            guessWordArr.append(Letter(i, 'green', guessWord))
        index += 1
    
    for letter in guessWordArr:
        if letter.status == 'red':
            print('{'+ letter.char + '}', end = '')
        elif letter.status == 'yellow':
            print('('+ letter.char + ')', end = '')
        else:
            print('['+ letter.char + ']', end = '')
    print()

    if gameWord == guessWordArr[0].word:
        win = True
        break












#hangman 2
import random

#find a given letter in the spring
#put the indexs found into a list
def find_letter(letter, word):

    indexsFound = []
    for index in range(len(word)):
        if letter.lower() == word[index].lower():
            indexsFound.append(index)

    return indexsFound

def replaceLetter(index, letter, string):
    # 1 convert the string into a list
    # 2 remove the index at which requested
    # 3 incert at the index requested with the letter
    # 4 convert list to string

    #1
    list_string = list(string)
    #2
    del list_string[index]
    #3
    list_string.insert(index, letter)

    #4
    outputWord = ""
    for index in list_string:
        outputWord += index

    #print(outputWord)
    return outputWord
    
stage = 0
def buildMan(stage):
    run = True
    if stage == 0:
        for _ in range(8):  print("")
        
    elif stage == 1:
        print("  O")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("_/ \_")

    elif stage == 2:
        print("  O--------O")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("_/ \_")
    elif stage == 3:
        print("  O--------O")
        print("  |        |")
        print("  |        0")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("_/ \_")
    elif stage == 4:
        print("  O--------O")
        print("  |        |")
        print("  |        0")
        print("  |	   |")
        print("  |	  -o-")
        print("  |")
        print("  |")
        print("_/ \_")
    elif stage == 5:
        print("  O--------O")
        print("  |        |")
        print("  |        0")
        print("  |	   |")
        print("  |	  -o-")
        print("  |        |")
        print("  |       / \\")
        print("_/ \_")
        run = False

    return stage + 1, run


#randomises a word
def word_generator():
    words = ["Dave", "Elliot", "Rivre", "fat", "infectious", "froward", "three", "inch", "scurvy", "scullion", "wert", "worm", "fool", "Nathan"]
    index = random.randint(0, len(words) - 1)
    return words[index]

word = word_generator()
outputWord = "_" * len(word)
run = True

while run:

    print(outputWord)
    print("")

    #check to see if it is spelt correctly
    if outputWord.lower() == word.lower():
        print("Well done, you have successfully guessed the word!")
        exit()

    user_input = input("Guess a letter: ")

    indexsFound = find_letter(user_input, word)

    if indexsFound == []:
        stage, run = buildMan(stage)    #build the hangman

    else:
        for indexReplace in indexsFound:
            outputWord = replaceLetter(indexReplace, word[indexReplace], outputWord)


print("You loose! The word was: {}".format(word))

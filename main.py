import random
import tkinter

def print_wordbank(wordbank):
    for i in range(0, len(wordbank),10):
        print('   '.join(wordbank[i:i+10]))

def check_guess(pguess, wordleword):
    print(check_red(pguess, wordleword))
    print(check_yellow(pguess, wordleword))
    print(check_green(pguess, wordleword))



def check_green(pguess, wword):
    index = 0
    gyx_index = 0
    pg = pguess
    temp_word = wword
    for letter in pguess:
        if letter == temp_word[index]:
            pg = pg[:index] + pg[index+1:]
            temp_word = temp_word[:index] + temp_word[index+1:]
            gyx[gyx_index] = "g"
        else:
            index += 1
        gyx_index +=1
    return gyx


def check_yellow(pguess,wword):
    index = 0
    gyx_index = 0
    temp_word = wword
    for letter in pguess:
        if letter in temp_word:
            temp_word = temp_word.replace(letter, " ", 1)
            gyx[gyx_index] = "y"
        else:
            index += 1
        gyx_index += 1

    return gyx

def check_red(pguess, wword):
    gyx_index = 0
    for letter in pguess:
        if letter not in wword:
            gyx[gyx_index] = "x"
        gyx_index += 1
    return gyx

words = open("wordbank.txt","r") 
wordbank = words.read()
wordbank = wordbank.split()
all_words = wordbank
round = 1
gyx = [" ", " ", " ", " ", " "]
word = random.choice(all_words)
print_wordbank(wordbank)
# print(word)

while round <= 5:
    guess = input("pick any 5 letter word: ")
    while len(guess) != 5:
        guess = input("pick any FIVE letter word: ")
    check_guess(guess,word)
    if gyx == ["g", "g", "g", "g", "g"]:
        print("you win")
        break
    gyx = [" ", " ", " ", " ", " "]



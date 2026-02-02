import random
import tkinter



def print_wordbank(wordbank):
    for i in range(0, len(wordbank),10):
        print('   '.join(wordbank[i:i+10]))

def check_guess(pguess, wordleword):
    print(check_green(pguess, wordleword))
    # check_yellow(pguess, wordleword)
    # check_red(pguess, wordleword)

def check_green(pguess, wword):
    index = 0
    temp_word = wword
    for letter in pguess:
        if letter == temp_word[index]:
            pguess = pguess[:index] + pguess[index+1:]
            wword = wword[:index] + wword[index+1:]
            gyx[index] = "g"
        index += 1
    return wword, gyx, pguess


def check_yellow(pguess,wword):
    index = 0
    temp_word = wword
    for letter in pguess:
        if letter == temp_word[index]:
            pguess[index] = ""
            word[index] = ""
        index += 1

def check_red(pguess, wword):
    index = 0
    temp_word = wword
    for letter in pguess:
        if letter == temp_word[index]:
            pguess[index] = ""
            word[index] = ""
        index += 1



words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.
all_words = wordbank
round = 1
gyx = [" ", " ", " ", " ", " "]
word = random.choice(all_words)
print_wordbank(wordbank)
print(word)

while round <= 5:
    guess = input("pick any 5 letter word: ")
    while len(guess) != 5:
        guess = input("pick any FIVE letter word: ")
    check_guess(guess,word)

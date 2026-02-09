def print_wordbank(wordbank):
    for i in range(0, len(wordbank),10):
        print('   '.join(wordbank[i:i+10]))

def contains_only_gyx(check_letters):
    print(check_letters)
    for char in check_letters:
        if char not in ["g", "x", "y"]:
            return False
    return True
              
def check_words(new_guess, gyx, available_words):
    good_letters = []
    i = 0
    for char in gyx:
        if char == "g":
            new_word_bank = []
            for word in available_words:
                if new_guess[i] in word[i]:
                    new_word_bank.append(word)
                    good_letters.append(new_guess[i])
            available_words = new_word_bank
        i += 1
    i = 0
    for char in gyx:
        if char == "y":
            new_word_bank = []
            for word in available_words:
                if new_guess[i] in word and not new_guess[i] in word[i]:
                    new_word_bank.append(word)
                    good_letters.append(new_guess[i])
            available_words = new_word_bank
        i += 1

    i = 0
    for char in gyx:
        if char == "x":
            new_word_bank = []
            for word in available_words:
                if not new_guess[i] in word or new_guess[i] in good_letters:
                    new_word_bank.append(word)
            available_words = new_word_bank
        i += 1
    return available_words                  

'''
Import New York Times' wordbank
'''
words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.
all_words = wordbank
print_wordbank(wordbank)

round = 1
while round <= 6:
    print("ROUND ", round)
    guess = input("what is your guess?: ")
    while not guess.isalpha or not guess in all_words:
        guess = input("error pick new word: ")
    correct_letters = input("which letter(s) are correct/ incorrect (g/y/x): ")
    print(len(correct_letters))
    while not contains_only_gyx(correct_letters) or len(correct_letters) != 5:
        correct_letters = input("which letter(s) is correct/ incorrect (g/y/x): ")
    wordbank = check_words(guess, correct_letters, wordbank)
    print_wordbank(wordbank)
    if len(wordbank) == 1:
        print("you found the word")
        break
    round += 1
if round > 6:
    print("you lose")

    
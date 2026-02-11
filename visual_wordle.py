import random
import tkinter as tk
from tkinter import messagebox

def print_wordbank(wordbank):
    for i in range(0, len(wordbank), 10):
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
        gyx_index += 1
    return gyx

def check_yellow(pguess, wword):
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

words = open("wordbank.txt", "r")
wordbank = words.read()
wordbank = wordbank.split()
all_words = wordbank

round = 1
gyx = [" ", " ", " ", " ", " "]
word = random.choice(all_words)
print_wordbank(wordbank)

class WordleGUI:
    def __init__(self, root):
        global round, gyx, word
        
        self.root = root
        self.root.title("Wordle Game")
        self.root.geometry("500x600")
        
        title_label = tk.Label(root, text="WORDLE", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        self.round_label = tk.Label(root, text=f"Round: {round}/5", font=("Arial", 14))
        self.round_label.pack()
        
        self.guesses_frame = tk.Frame(root)
        self.guesses_frame.pack(pady=20)
        
        self.guess_displays = []
        
       
        input_frame = tk.Frame(root)
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Enter your guess:", font=("Arial", 12)).pack()
        
        self.entry = tk.Entry(input_frame, font=("Arial", 16), width=10)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda e: self.submit_guess())
        
     
        self.submit_button = tk.Button(input_frame, text="Submit Guess", command=self.submit_guess, font=("Arial", 12))
        self.submit_button.pack()
        
      
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
    def submit_guess(self):
        global round, gyx, word
        
        guess = self.entry.get().lower()
        
        if len(guess) != 5:
            self.result_label.config(text="Please enter a FIVE letter word!", fg="red")
            return
        
       
        gyx = [" ", " ", " ", " ", " "]
        

        check_guess(guess, word)
        
       
        self.display_guess(guess, gyx)
        
     
        if gyx == ["g", "g", "g", "g", "g"]:
            messagebox.showinfo("Congratulations!", "You win!")
            self.entry.config(state='disabled')
            self.submit_button.config(state='disabled')
            return
        
        round += 1
        self.round_label.config(text=f"Round: {round}/5")
        
       
        if round > 5:
            messagebox.showinfo("Game Over", f"You lose! The word was: {word}")
            self.entry.config(state='disabled')
            self.submit_button.config(state='disabled')
            return
        
       
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def display_guess(self, guess, gyx):
        
        guess_frame = tk.Frame(self.guesses_frame)
        guess_frame.pack()
        
       
        for i, letter in enumerate(guess):
            color = "gray"
            if gyx[i] == "g":
                color = "green"
            elif gyx[i] == "y":
                color = "yellow"
            elif gyx[i] == "x":
                color = "darkgray"
            
            letter_label = tk.Label(guess_frame, text=letter.upper(), 
                                   bg=color, width=4, height=2,
                                   font=("Arial", 16, "bold"),
                                   relief="solid", borderwidth=2)
            letter_label.pack(side=tk.LEFT, padx=2)

root = tk.Tk()
app = WordleGUI(root)
root.mainloop()
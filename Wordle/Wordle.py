import WordList
import random
from tkinter import *
from tkinter import messagebox

# symbols = [r'''
#  __
# |\/|
# |/\|
#  -- ''', r'''
#  __
# |  |
# |  |
#  -- ''',r'''
#  __
# |\ |
# | \|
#  -- ''']
#
# choosen_word=random.choice(WordList.five_letter_words).lower()
# word =[]
# for letter1 in choosen_word:
#     word.append(letter1)
#
# letters_yellow=[]
# letters_gray=[]
#
# guesses=5
#
#
# game_over=False
#
# while not game_over:
#     display=""
#     guess=input("What is your guess\n").lower()
#     if guess in WordList.five_letter_words or guess in WordList.five_letter_words2:
#
#         guess_list=[]
#         for letter2 in guess:
#             guess_list.append(letter2)
#
#         correct_letter = []
#
#         for position in range (0,5):
#             if guess_list[position]==word[position]:
#                 display+=word[position]
#                 correct_letter.append(word[position])
#                 print (symbols[0])
#                 if word[position] not in letters_yellow:
#                     letters_yellow.append(word[position])
#
#             elif guess_list[position] in word:
#                 print(symbols[2])
#                 display+="_"
#                 if word[position] not in letters_yellow:
#                     letters_yellow.append(word[position])
#
#             else:
#                 print(symbols[1])
#                 display+="_"
#                 if word[position] not in letters_gray:
#                     letters_gray.append(word[position])
#
#         print(f"The word is:  {display}")
#
#         print(f"YELLOW OR GREEN letters: {letters_yellow}")
#         print(f"GRAY letters: {letters_gray}")
#
#         if correct_letter == word:
#             game_over=True
#             print("****************** You win! You guessed the word! ******************")
#             exit(0)
#
#         guesses-=1
#         if guesses==0:
#             game_over=True
#             print("****************** You lose, you ran out of guesses ******************")
#             print(f"****************** The word was:{choosen_word} ******************")
#             exit(0)
#
#     else:
#         print("Your word is not accepted, please try another word")
#

row=-1
guesses=5

GREEN = "#9bdeac"
YELLOW = "#F9DC5C"
GRAY="#CAD5CA"


## Make a guess
def process_guess():
    global row, guesses
    guess_s=guess_entry.get().lower()
    guess_list = [letter for letter in guess_s]
    correct_letter=[]

    row+=1
    column=0
    guess_entry.delete(0, END)

    if len(guess_s) != 5:
        messagebox.showinfo(title="No", message="Please enter a 5 letter word")
        return

    if guess_s.lower() not in WordList.five_letter_words2 and guess_s.title() not in WordList.five_letter_words:
        messagebox.showinfo(title="No", message="Looks like the word you entered doesn't exist")
        return

    if guesses > 0:
        for position in range (0,5):
            column+=1
            if guess_list[position]==word[position]:
                if guess_list[position] not in correct_letter:
                    correct_letter.append(word[position])
                letter_display=Canvas(width=58, height=58, bg=GREEN)
                letter_display.create_text(23,23, text=word[position].upper(), fill="white", font=("Courier", 30, "bold"))
                letter_display.grid(row=row, column=column)

            elif guess_list[position] in word:
                letter_display = Canvas(width=58, height=58, bg=YELLOW)
                letter_display.create_text(23, 23, text=guess_list[position].upper(), fill="white", font=("Courier", 30, "bold"))
                letter_display.grid(row=row, column=column)

            else:
                letter_display = Canvas(width=58, height=58, bg=GRAY)
                letter_display.create_text(23, 23, text=guess_list[position].upper(), fill="white", font=("Courier", 30, "bold"))
                letter_display.grid(row=row, column=column)

        if len(correct_letter) == 5:
            messagebox.showinfo(title="WIN", message="YAYY YOU GOT THE WORD!")
        guesses -= 1
        guess_left2.config(text=f"{guesses}")

    else:
        messagebox.showinfo(title="GAME OVER", message="Looks like you ran out of Guesses. GAME OVER.")


## User Interface

window=Tk()
window.title("Wordle")

guess=Label(text="Guess:", font=("Courier", 30, "bold"))
guess.grid(row=6, column=0)
guess_entry=Entry()
guess_entry.focus()
guess_entry.grid(row=6, column=1, columnspan=4, sticky="EW")

guess_left=Label(text=f"Guesses left", font=("Courier", 15, "bold"))
guess_left.grid(column=0, row=0)
guess_left2=Label(text=f"{guesses}", font=("Courier", 15, "bold"))
guess_left2.grid(column=0, row=1)

button=Button(text="Try", command=process_guess, font=("Courier", 15, "bold"))
button.grid(row=7, column=2, columnspan=2)

# background=Canvas(width=350, height=440, highlightthickness=0)
# bgimage=PhotoImage(file="Screenshot 2025-11-16 121306.png")
# background.create_image(175,220, image=bgimage)
# background.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="NE")

choosen_word=random.choice(WordList.five_letter_words).lower()
word = [letter for letter in choosen_word]


window.mainloop()













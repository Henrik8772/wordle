import tkinter as tk
from tkinter import messagebox
from tkinter import *


word = "gurka"


def guess():
    current = guess_var.get().strip().lower()
    if current == word:
        print(current)
        messagebox.showinfo("Result", "You Win YIPPIEEEE!!!!!")
    else:
        guess_var.set("")


wordle = Tk()

button_frame = Frame(wordle)
button_frame.pack(pady=5)

guess_var = StringVar()
type_guess = Entry(button_frame, textvariable=guess_var)
type_guess.grid(row=0, column=0, padx=5)
Button(button_frame, text="Guess", width=5,
       command=guess).grid(row=0, column=1, padx=5)

mainloop()

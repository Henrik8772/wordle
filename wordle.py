import tkinter as tk
from tkinter import messagebox
from tkinter import *


word = "gurka"


def guess():
    print(type_guess)
    if type_guess == word:
        messagebox.INFO = "You Win YIPPIEEEE!!!!!"
    if type_guess != word:
        guess_var.set("")


wordle = Tk()

button_frame = Frame(wordle)
button_frame.pack(pady=5)

guess_var = StringVar()
type_guess = Entry(button_frame, textvariable=guess_var).grid(
    row=0, column=0, padx=5)
Button(button_frame, text="Guess", width=5,
       command=guess).grid(row=0, column=1, padx=5)

mainloop()

import tkinter as tk


def printFrame(frame, text):
    tk.Label(
        frame, text=text, font=("Courier", 12), wraplength=600, justify=tk.LEFT
    ).grid(sticky=tk.W)

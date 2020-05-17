import tkinter as tk


def printFrame(frame, text):
    tk.Label(frame, text=text, font=("Courier", 12),).grid(sticky=tk.W)

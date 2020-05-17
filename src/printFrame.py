import tkinter as tk


def printFrame(frame, text):
    tk.Label(
        frame, text=text, font=("Courier", 12), wraplength=600, justify=tk.LEFT
    ).grid(sticky=tk.W)


def printHelp(frame, text, row):
    tk.Label(
        frame,
        text=text,
        font=("Helvetica", 14),
        wraplength=600,
        justify=tk.LEFT,
    ).grid(sticky=tk.W, row=row)


def printTableHeader(frame, col1, col2, row):
    tk.Label(
        frame, text=col1, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.E, column=0, row=row)
    tk.Label(
        frame, text=col2, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.W, column=1, row=row)


def printTableRow(frame, col1, col2, row):
    tk.Label(frame, text=col1, font=("Helvetica", 14), justify=tk.LEFT,).grid(
        sticky=tk.E, column=0, row=row
    )
    tk.Label(frame, text=col2, font=("Courier", 14), justify=tk.LEFT,).grid(
        sticky=tk.W, column=1, row=row
    )

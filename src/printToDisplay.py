import os
import tkinter as tk

from PIL import Image, ImageTk


def printFrame(frame, text):
    print(text)
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


def printTableHeader(frame, col1, col2, col3, row):
    tk.Label(
        frame, text=col1, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.E, column=0, row=row)

    tk.Label(
        frame, text=col2, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.E, column=1, row=row)

    tk.Label(
        frame, text=col3, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.W, column=2, row=row)


def printTableRow(frame, col1, col2, col3, row):
    tk.Label(frame, text=col1, font=("Helvetica", 14), justify=tk.LEFT,).grid(
        sticky=tk.E, column=0, row=row
    )

    img = Image.open(os.path.join(os.getcwd(), "src", "img", col2))
    ph = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=ph,)
    label.grid(column=1, row=row)
    label.image = ph

    tk.Label(frame, text=col3, font=("Courier", 14), justify=tk.LEFT,).grid(
        sticky=tk.W, column=2, row=row
    )


def printExampleHeader(frame, col1, col2, row):
    tk.Label(
        frame, text=col1, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.E, column=0, row=row)

    tk.Label(
        frame, text=col2, font=("Helvetica", 14, "bold"), justify=tk.LEFT,
    ).grid(sticky=tk.W, column=1, row=row)


def printExampleRow(frame, col1, col2, row):
    img = Image.open(os.path.join(os.getcwd(), "src", "img", col1))
    ph = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=ph,)
    label.grid(
        column=0, row=row, sticky=tk.E,
    )
    label.image = ph

    tk.Label(frame, text=col2, font=("Courier", 14), justify=tk.LEFT,).grid(
        sticky=tk.W, column=1, row=row
    )

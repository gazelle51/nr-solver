import src.nrSingle as nrSingle
import src.nrMultiple as nrMultiple

# import tkinter as tk

# NR Single
nrSingle.newtonRaphsonSingleVariable("15*((x-4)/7) + (sin(5*x))**3", "x", 2)

# NR Multiple
nrMultiple.newtonRaphsonTwoVariables(
    "10*x*sin(y) + 0.5", "10*x**2 - 10*x*cos(y) + 0.2", "x", "y", 1, 0, 0.001
)

import math
import src.nrSingle as nrSingle

# Function to find roots for
def f1(x):
    return 15 * ((x - 4) / 7) + (math.sin(5 * x)) ** 3


# Derivative of above function
def df1(x):
    return 15 / 7 + 15 * ((math.sin(5 * x)) ** 2) * math.cos(5 * x)


# Driver program to test above
nrSingle.newtonRaphsonSingleVariable(
    2, f1, df1,
)

import math
import src.nrSingle as nrSingle
import src.nrMultiple as nrMultiple

# NR Single
nrSingle.newtonRaphsonSingleVariable("15*((x-4)/7) + (sin(5*x))**3", "x", 2)

# Function to find roots for
def f2(x, y):
    return 10 * x * math.sin(y) + 0.5


def f3(x, y):
    return 10 * x ** 2 - 10 * x * math.cos(y) + 0.2


def df2dx(x, y):
    return 10 * math.sin(y)


def df2dy(x, y):
    return 10 * x * math.cos(y)


def df3dx(x, y):
    return 20 * x - 10 * math.cos(y)


def df3dy(x, y):
    return 10 * x * math.sin(y)


nrMultiple.newtonRaphsonTwoVariables(
    1, 0, f2, f3, df2dx, df2dy, df3dx, df3dy, 0.001
)

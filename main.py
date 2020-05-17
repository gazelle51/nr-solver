import src.nrSingle as nrSingle
import src.nrTwo as nrTwo
from src.printFrame import *

import tkinter as tk
from tkscrolledframe import ScrolledFrame


class MyApp:
    def __init__(self):
        self.TITLE = "Newton Raphson Method Solver"

        self.root = tk.Tk()
        self.root.title(self.TITLE)
        self.root.iconphoto(False, tk.PhotoImage(file="./src/icon.png"))

        self.header().grid(row=0, padx=10)
        self.nrSingle().grid(row=1, padx=10, pady=5)
        self.nrTwo().grid(row=2, padx=10, pady=5)
        self.footer().grid(row=3, padx=10, pady=5)

    def header(self):
        frame = tk.Frame(self.root)

        tk.Label(frame, text=self.TITLE, font=("Helvetica", 20, "bold"),).grid(
            row=0, pady=10
        )

        return frame

    def nrSingle(self):
        frame = tk.Frame(self.root)

        tk.Label(
            frame,
            text="Single Variable Method",
            font=("Helvetica", 15, "bold"),
        ).grid(row=0, columnspan=2)

        tk.Label(frame, text="Equation").grid(row=1, sticky=tk.E)
        tk.Label(frame, text="Variable").grid(row=2, sticky=tk.E)
        tk.Label(frame, text="Initial guess").grid(row=3, sticky=tk.E)
        tk.Label(frame, text="\u03B5").grid(row=4, sticky=tk.E)

        self.eqSingle = tk.Entry(frame)
        self.eqSingle.insert(0, "15*((x-4)/7) + (sin(5*x))**3")
        self.eqSingle.grid(row=1, column=1)

        self.varSingle = tk.Entry(frame)
        self.varSingle.insert(0, "x")
        self.varSingle.grid(row=2, column=1)

        self.initGuessSingle = tk.Entry(frame)
        self.initGuessSingle.insert(0, 2)
        self.initGuessSingle.grid(row=3, column=1)

        self.epsSingle = tk.Entry(frame)
        self.epsSingle.insert(0, 0.001)
        self.epsSingle.grid(row=4, column=1)

        tk.Button(frame, text="GO", fg="blue", command=self.runNrSingle).grid(
            row=5, column=1, sticky=tk.W
        )

        return frame

    def nrTwo(self):
        frame = tk.Frame(self.root)

        tk.Label(
            frame, text="Two Variable Method", font=("Helvetica", 15, "bold"),
        ).grid(row=0, columnspan=2)

        tk.Label(frame, text="Equation 1").grid(row=1, sticky=tk.E)
        tk.Label(frame, text="Equation 2").grid(row=2, sticky=tk.E)
        tk.Label(frame, text="Variable 1").grid(row=3, sticky=tk.E)
        tk.Label(frame, text="Variable 2").grid(row=4, sticky=tk.E)
        tk.Label(frame, text="Initial guess for variable 1").grid(
            row=5, sticky=tk.E
        )
        tk.Label(frame, text="Initial guess for variable 2").grid(row=6)
        tk.Label(frame, text="\u03B5").grid(row=7, sticky=tk.E)

        self.eq1Two = tk.Entry(frame)
        self.eq1Two.insert(0, "10*x*sin(y) + 0.5")
        self.eq1Two.grid(row=1, column=1)

        self.eq2Two = tk.Entry(frame)
        self.eq2Two.insert(0, "10*x**2 - 10*x*cos(y) + 0.2")
        self.eq2Two.grid(row=2, column=1)

        self.var1Two = tk.Entry(frame)
        self.var1Two.insert(0, "x")
        self.var1Two.grid(row=3, column=1)

        self.var2Two = tk.Entry(frame)
        self.var2Two.insert(0, "y")
        self.var2Two.grid(row=4, column=1)

        self.initGuess1Two = tk.Entry(frame)
        self.initGuess1Two.insert(0, 1)
        self.initGuess1Two.grid(row=5, column=1)

        self.initGuess2Two = tk.Entry(frame)
        self.initGuess2Two.insert(0, 0)
        self.initGuess2Two.grid(row=6, column=1)

        self.epsTwo = tk.Entry(frame)
        self.epsTwo.insert(0, 0.001)
        self.epsTwo.grid(row=7, column=1)

        tk.Button(frame, text="GO", fg="blue", command=self.runNrTwo,).grid(
            row=8, column=1, sticky=tk.W
        )

        return frame

    def footer(self):
        frame = tk.Frame(self.root)

        tk.Button(frame, text="HELP", fg="grey", command=self.helpWindow).grid(
            row=0, column=0, sticky=tk.W
        )
        tk.Button(frame, text="QUIT", fg="black", command=quit).grid(
            row=0, column=1, sticky=tk.E
        )

        return frame

    def createScrollFrame(self, parent, width=600, height=500):
        sf = ScrolledFrame(parent, width=width, height=height)
        sf.grid(row=0)
        sf.bind_arrow_keys(self.root)
        sf.bind_scroll_wheel(self.root)

        frame = sf.display_widget(tk.Frame)

        return frame

    def runNrSingle(self):
        singleWindow = tk.Toplevel(self.root)

        # Scroll frame
        output = self.createScrollFrame(singleWindow)
        output.grid(padx=5)
        printFrame(
            output, "Starting Newton Raphson Method for a single variable"
        )
        printFrame(
            output,
            "Solving {}=0 for {} with an initial guess of {}={} to an accuracy of {}".format(
                self.eqSingle.get(),
                self.varSingle.get(),
                self.varSingle.get(),
                self.initGuessSingle.get(),
                self.epsSingle.get(),
            ),
        )

        # Close button
        close = tk.Frame(singleWindow)
        close.grid(row=1, pady=5)
        tk.Button(
            close, text="CLOSE", fg="black", command=singleWindow.destroy
        ).grid(sticky=tk.W)

        nrSingle.newtonRaphsonSingleVariable(
            output,
            self.eqSingle.get(),
            self.varSingle.get(),
            float(self.initGuessSingle.get()),
            float(self.epsSingle.get()),
        )

    def runNrTwo(self):
        singleWindow = tk.Toplevel(self.root)

        # Scroll frame
        output = self.createScrollFrame(singleWindow)
        output.grid(padx=5)
        printFrame(output, "Starting Newton Raphson Method for two variables")
        printFrame(
            output,
            "Solving {}=0 and {}=0 for {} and {} with an initial guess of {}={} and {}={} to an accuracy of {}".format(
                self.eq1Two.get(),
                self.eq2Two.get(),
                self.var1Two.get(),
                self.var2Two.get(),
                self.var1Two.get(),
                self.initGuess1Two.get(),
                self.var2Two.get(),
                self.initGuess2Two.get(),
                self.epsTwo.get(),
            ),
        )

        # Close button
        close = tk.Frame(singleWindow)
        close.grid(row=1, pady=5)
        tk.Button(
            close, text="CLOSE", fg="black", command=singleWindow.destroy
        ).grid(sticky=tk.W)

        nrTwo.newtonRaphsonTwoVariables(
            output,
            self.eq1Two.get(),
            self.eq2Two.get(),
            self.var1Two.get(),
            self.var2Two.get(),
            float(self.initGuess1Two.get()),
            float(self.initGuess2Two.get()),
            float(self.epsTwo.get()),
        )

    def helpWindow(self):
        win = tk.Toplevel(self.root)

        # Scroll frame
        main = self.createScrollFrame(win)
        main.grid(padx=5)

        # Help for single variable
        tk.Label(
            main,
            text="Single Variable Method",
            font=("Helvetica", 15, "bold"),
        ).grid(row=0)
        printHelp(
            main,
            'To use the NR method to solve an equation with a single unknown variable, use the "Single Variable Method" section of this application. You need to fill in the equation, the unknown variable, an initial guess for the unknown variable and an epsilon threshold value. An example is already pre-loaded for your reference.',
            row=1,
        )

        # Help for two variables
        tk.Label(
            main, text="Two Variable Method", font=("Helvetica", 15, "bold"),
        ).grid(row=2)
        printHelp(
            main,
            'To use the NR method to solve a pair of simultaneous equations with two unknown variables, use the "Two Variable Method" section of this application. You need to fill in the two equations, the two unknown variables, an initial guess for each unknown variable and an epsilon threshold value. An example is already pre-loaded for your reference.',
            row=3,
        )

        # Help for equation formatting
        tk.Label(
            main,
            text="Formatting the Equations",
            font=("Helvetica", 15, "bold"),
        ).grid(row=4)
        printHelp(
            main,
            "This section explains how to format your equations. The syntax for various functions is listed below.",
            row=5,
        )

        # Table
        table = tk.Frame(main)
        table.grid(row=6)
        printTableHeader(table, "Function", "Syntax", row=0)
        printTableRow(table, "Addition", "+", row=1)
        printTableRow(table, "Subtraction", "-", row=2)
        printTableRow(table, "Multiplication", "*", row=3)
        printTableRow(table, "Division", "/", row=4)
        printTableRow(table, "Exponent / to the power of", "**", row=5)
        printTableRow(table, "Square root", "sqrt(x)", row=6)
        printTableRow(table, "Cubed root", "cbrt(x)", row=7)
        printTableRow(table, "nth root", "root(x, n) OR x**(1/n)", row=8)
        printTableRow(table, "Pi, \u03C0", "pi", row=9)
        printTableRow(table, "Euler's number, e^x", "exp(x)", row=10)
        printTableRow(table, "Natural log", "log(x)", row=11)
        printTableRow(table, "Log with base b", "log(x, b)", row=12)
        printTableRow(table, "Sine", "sin(x)", row=13)
        printTableRow(table, "Cosine", "cos(x)", row=14)
        printTableRow(table, "Tangent", "tan(x)", row=15)
        printTableRow(table, "Inverse sine", "asin(x)", row=16)
        printTableRow(table, "Inverse cosine", "acos(x)", row=17)
        printTableRow(table, "Inverse tangent", "atan(x)", row=18)

        # Close button
        close = tk.Frame(win)
        close.grid(row=1, pady=5)
        tk.Button(close, text="CLOSE", fg="black", command=win.destroy).grid()


app = MyApp()
app.root.mainloop()

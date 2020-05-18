import src.nrSingle as nrSingle
import src.nrTwo as nrTwo
from src.printToDisplay import *
from src.scrolledFrame import *

import tkinter as tk


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

    def runNrSingle(self):
        singleWindow = tk.Toplevel(self.root)

        # Scroll frame
        frame = Tkscrolledframe(singleWindow, width=600, height=500)
        frame.grid(row=0)
        output = frame.getFrame()
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

        nrSingle.newtonRaphsonSingleVariable(
            output,
            self.eqSingle.get(),
            self.varSingle.get(),
            float(self.initGuessSingle.get()),
            float(self.epsSingle.get()),
        )

        frame.update()

        # Close button
        close = tk.Frame(singleWindow)
        close.grid(row=1, pady=5)
        tk.Button(
            close, text="CLOSE", fg="black", command=singleWindow.destroy
        ).grid(sticky=tk.W)

    def runNrTwo(self):
        singleWindow = tk.Toplevel(self.root)

        # Scroll frame
        frame = Tkscrolledframe(singleWindow, width=600, height=500)
        frame.grid(row=0)
        output = frame.getFrame()
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

        frame.update()

        # Close button
        close = tk.Frame(singleWindow)
        close.grid(row=1, pady=5)
        tk.Button(
            close, text="CLOSE", fg="black", command=singleWindow.destroy
        ).grid(sticky=tk.W)

    def helpWindow(self):
        win = tk.Toplevel(self.root)

        # Scroll frame
        frame = Tkscrolledframe(win, width=610, height=700)
        frame.grid(row=0)
        main = frame.getFrame()
        main.grid()

        tk.Label(main, text="Help", font=("Helvetica", 18, "bold"),).grid(
            row=0
        )

        # Help for single variable
        tk.Label(
            main,
            text="Single Variable Method",
            font=("Helvetica", 15, "bold"),
        ).grid(row=1, pady=(15, 0))
        printHelp(
            main,
            'To use the NR method to solve an equation with a single unknown variable, use the "Single Variable Method" section of this application. You need to fill in the equation, the unknown variable, an initial guess for the unknown variable and an epsilon threshold value. An example is already pre-loaded for your reference.',
            row=2,
        )
        frame.update()

        # Help for two variables
        tk.Label(
            main, text="Two Variable Method", font=("Helvetica", 15, "bold"),
        ).grid(row=3, pady=(15, 0))
        printHelp(
            main,
            'To use the NR method to solve a pair of simultaneous equations with two unknown variables, use the "Two Variable Method" section of this application. You need to fill in the two equations, the two unknown variables, an initial guess for each unknown variable and an epsilon threshold value. An example is already pre-loaded for your reference.',
            row=4,
        )
        frame.update()

        # Help for equation formatting
        tk.Label(
            main,
            text="Formatting the Equations",
            font=("Helvetica", 15, "bold"),
        ).grid(row=5, pady=(15, 0))
        printHelp(
            main,
            "This section explains how to format your equations. The syntax for various functions is listed below.",
            row=6,
        )
        frame.update()

        # Table
        table = tk.Frame(main)
        table.grid(row=7)
        printTableHeader(table, "Function", "Example", "Syntax", row=0)
        printTableRow(
            table, "Addition", "./src/img/plus.gif", "+", row=1,
        )
        printTableRow(table, "Subtraction", "./src/img/minus.gif", "-", row=2)
        printTableRow(
            table, "Multiplication", "./src/img/times.gif", "*", row=3
        )
        printTableRow(table, "Division", "./src/img/divide.gif", "/", row=4)
        printTableRow(
            table,
            "Exponent / to the power of",
            "./src/img/a_to_b.gif",
            "a ** b",
            row=5,
        )
        printTableRow(
            table, "Square root", "./src/img/root_x.gif", "sqrt(x)", row=6
        )
        printTableRow(
            table, "Cubed root", "./src/img/root_3_x.gif", "cbrt(x)", row=7
        )
        printTableRow(
            table,
            "nth root",
            "./src/img/root_n_x.gif",
            "root(x, n) OR x**(1/n)",
            row=8,
        )
        printTableRow(table, "Pi, \u03C0", "./src/img/pi.gif", "pi", row=9)
        printTableRow(
            table, "Euler's number", "./src/img/e_x.gif", "exp(x)", row=10,
        )
        printTableRow(
            table, "Natural log", "./src/img/log.gif", "log(x)", row=11
        )
        printTableRow(
            table,
            "Log with base b",
            "./src/img/log_b.gif",
            "log(x, b)",
            row=12,
        )
        printTableRow(table, "Sine", "./src/img/sin.gif", "sin(x)", row=13)
        printTableRow(table, "Cosine", "./src/img/cos.gif", "cos(x)", row=14)
        printTableRow(table, "Tangent", "./src/img/tan.gif", "tan(x)", row=15)
        printTableRow(
            table, "Inverse sine", "./src/img/asin.gif", "asin(x)", row=16
        )
        printTableRow(
            table, "Inverse cosine", "./src/img/acos.gif", "acos(x)", row=17
        )
        printTableRow(
            table, "Inverse tangent", "./src/img/atan.gif", "atan(x)", row=18
        )
        frame.update()

        # Examples
        printHelp(
            main,
            "\nIt it also useful to use brackets to make sure your function is formatted correctly. There are some examples below.",
            row=8,
        )
        examples = tk.Frame(main)
        examples.grid(row=9)

        printExampleHeader(examples, "Function", "Input Syntax", row=0)
        printExampleRow(
            examples, "./src/img/eg1.gif", "(sin(x))**2 - exp(4/x)", row=1
        )
        printExampleRow(
            examples,
            "./src/img/eg2.gif",
            "15*((x-4)/7) + (sin(5*x))**3",
            row=2,
        )
        printExampleRow(
            examples, "./src/img/eg3.gif", "10*x*sin(y) + 0.5", row=3
        )
        printExampleRow(
            examples, "./src/img/eg4.gif", "10*x**2 - 10*x*cos(y) + 0.2", row=4
        )
        frame.update()

        # Close button
        close = tk.Frame(win)
        close.grid(row=1, pady=5)
        tk.Button(close, text="CLOSE", fg="black", command=win.destroy).grid()


app = MyApp()
app.root.mainloop()

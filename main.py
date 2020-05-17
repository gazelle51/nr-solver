import src.nrSingle as nrSingle
import src.nrTwo as nrTwo
from src.printFrame import printFrame

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

        tk.Button(frame, text="QUIT", fg="black", command=quit).grid(row=16)

        return frame

    def createScrollFrame(self, parent, width=500, height=500):
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
        close.grid(row=1)
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
        close.grid(row=1)
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


app = MyApp()
app.root.mainloop()

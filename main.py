import src.nrSingle as nrSingle
import src.nrTwo as nrTwo

import tkinter as tk


class MyApp:
    def __init__(self):

        self.root = tk.Tk()
        # self.root.geometry("500x900")  # Width x Height

        self.header()
        self.nrSingle()
        self.nrTwo()
        self.footer()

    def header(self):
        tk.Label(
            self.root,
            text="Newton Raphson Method Solver",
            font=("Helvetica", 20, "bold"),
        ).grid(row=0, pady=10)

    def nrSingle(self):
        tk.Label(
            self.root,
            text="Single Variable Method",
            font=("Helvetica", 15, "bold"),
        ).grid(row=1)

        tk.Label(self.root, text="Equation").grid(row=2)
        tk.Label(self.root, text="Variable").grid(row=3)
        tk.Label(self.root, text="Initial guess").grid(row=4)

        self.eqSingle = tk.Entry(self.root)
        self.eqSingle.insert(0, "15*((x-4)/7) + (sin(5*x))**3")
        self.eqSingle.grid(row=2, column=1)

        self.varSingle = tk.Entry(self.root)
        self.varSingle.insert(0, "x")
        self.varSingle.grid(row=3, column=1)

        self.initGuessSingle = tk.Entry(self.root)
        self.initGuessSingle.insert(0, 2)
        self.initGuessSingle.grid(row=4, column=1)

        tk.Button(
            self.root, text="GO", fg="red", command=self.runNrSingle
        ).grid(row=5)

    def nrTwo(self):
        tk.Label(
            self.root,
            text="Two Variable Method",
            font=("Helvetica", 15, "bold"),
        ).grid(row=6)

        tk.Label(self.root, text="Equation 1").grid(row=7)
        tk.Label(self.root, text="Equation 2").grid(row=8)
        tk.Label(self.root, text="Variable 1").grid(row=9)
        tk.Label(self.root, text="Variable 2").grid(row=10)
        tk.Label(self.root, text="Initial guess for variable 1").grid(row=11)
        tk.Label(self.root, text="Initial guess for variable 2").grid(row=12)

        self.eq1Two = tk.Entry(self.root)
        self.eq1Two.insert(0, "10*x*sin(y) + 0.5")
        self.eq1Two.grid(row=7, column=1)

        self.eq2Two = tk.Entry(self.root)
        self.eq2Two.insert(0, "10*x**2 - 10*x*cos(y) + 0.2")
        self.eq2Two.grid(row=8, column=1)

        self.var1Two = tk.Entry(self.root)
        self.var1Two.insert(0, "x")
        self.var1Two.grid(row=9, column=1)

        self.var2Two = tk.Entry(self.root)
        self.var2Two.insert(0, "y")
        self.var2Two.grid(row=10, column=1)

        self.initGuess1Two = tk.Entry(self.root)
        self.initGuess1Two.insert(0, 1)
        self.initGuess1Two.grid(row=11, column=1)

        self.initGuess2Two = tk.Entry(self.root)
        self.initGuess2Two.insert(0, 0)
        self.initGuess2Two.grid(row=12, column=1)

        tk.Button(self.root, text="GO", fg="red", command=self.runNrTwo).grid(
            row=13
        )

    def footer(self):
        tk.Button(self.root, text="QUIT", fg="red", command=quit).grid(row=14)

    def runNrSingle(self):
        # TODO: add epsilon
        nrSingle.newtonRaphsonSingleVariable(
            self.eqSingle.get(),
            self.varSingle.get(),
            float(self.initGuessSingle.get()),
        )

    def runNrTwo(self):
        # TODO: add epsilon
        nrTwo.newtonRaphsonTwoVariables(
            self.eq1Two.get(),
            self.eq2Two.get(),
            self.var1Two.get(),
            self.var2Two.get(),
            float(self.initGuess1Two.get()),
            float(self.initGuess2Two.get()),
        )


app = MyApp()
app.root.mainloop()


# # NR Multiple
# nrTwo.newtonRaphsonTwoVariables(
#     "10*x*sin(y) + 0.5", "10*x**2 - 10*x*cos(y) + 0.2", "x", "y", 1, 0, 0.001
# )

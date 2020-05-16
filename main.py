import src.nrSingle as nrSingle
import src.nrTwo as nrTwo

import tkinter as tk


class MyApp:
    def __init__(self):

        self.root = tk.Tk()
        # self.root.geometry("500x900")  # Width x Height

        self.header()
        self.nrSingle()
        self.footer()

    def header(self):
        tk.Label(
            self.root,
            text="Newton Raphson Method Solver",
            font=("Helvetica", 20, "bold"),
        ).grid(row=0, pady=10)

    def nrSingle(self):
        singleTitle = tk.Label(
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

    def footer(self):
        tk.Button(self.root, text="QUIT", fg="red", command=quit).grid(row=6)

    def runNrSingle(self):
        nrSingle.newtonRaphsonSingleVariable(
            self.eqSingle.get(),
            self.varSingle.get(),
            float(self.initGuessSingle.get()),
        )

    def runNrTwo(self):
        nrTwo.newtonRaphsonTwoVariables(
            self.eqSingle.get(),
            self.varSingle.get(),
            float(self.initGuessSingle.get()),
        )


app = MyApp()
app.root.mainloop()


# # NR Multiple
# nrTwo.newtonRaphsonTwoVariables(
#     "10*x*sin(y) + 0.5", "10*x**2 - 10*x*cos(y) + 0.2", "x", "y", 1, 0, 0.001
# )

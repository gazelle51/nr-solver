import numpy as np
import sympy as sym
from src.printFrame import printFrame


def newtonRaphsonTwoVariables(
    frame, f, g, symbol1, symbol2, initVal1, initVal2, eps=0.0001
):
    """Use the Newton Raphson method to find the solution to two simultaneous 
    equations with two variables.
    
    Args:
        frame (tk.Frame): frame to print output in
        f (str): the first function to find the solution of
        g (str): the second function to find the solution of
        symbol1 (str): symbol for the first unknown variable in the function
        symbol2 (str): symbol for the second unknown variable in the function
        initVal1 (float): initial guess for the x value of the solution
        initVal12 (float): initial guess for the y value of the solution
        eps (float): epsilon threshold value (default is 0.0001)

    Returns:
        float: Solution to the problem
    """

    # Initialisation
    i = 0  # Counter
    xyVal = np.array([[initVal1, initVal2]]).T  # Initial guesses for x and y
    xSym, ySym = sym.symbols([symbol1, symbol2])  # Symbols used for x and y
    f = sym.sympify(f)  # Convert function f to sympy
    g = sym.sympify(g)  # Convert function g to sympy
    dfdx = sym.diff(f, xSym)  # Derivative of f wrt x
    dfdy = sym.diff(f, ySym)  # Derivative of f wrt y
    dgdx = sym.diff(g, xSym)  # Derivative of g wrt x
    dgdy = sym.diff(g, ySym)  # Derivative of g wrt y

    def J(x, y):
        """Calculate and return the Jacobian matrix at a point."""

        return np.array(
            [
                [
                    dfdx.subs([(xSym, x), (ySym, y)]).evalf(),
                    dfdy.subs([(xSym, x), (ySym, y)]).evalf(),
                ],
                [
                    dgdx.subs([(xSym, x), (ySym, y)]).evalf(),
                    dgdy.subs([(xSym, x), (ySym, y)]).evalf(),
                ],
            ],
            dtype="float",
        )

    def delta():
        """Calculate and return the correction vector."""

        x = xyVal[0][0]
        y = xyVal[1][0]

        return np.matmul(
            -np.linalg.inv(J(x, y)),
            np.array(
                [
                    [f.subs([(xSym, x), (ySym, y)]).evalf()],
                    [g.subs([(xSym, x), (ySym, y)]).evalf()],
                ]
            ),
        )

    printFrame(
        frame,
        "\nIteration |       {} (7dp) |       {} (7dp)".format(
            symbol1, symbol2
        ),
    )
    printFrame(frame, "==========================================")

    # Start looping
    while (np.abs(delta()) >= eps).any():
        printFrame(
            frame,
            "    {:5d} | {: 13.7f} | {: 13.7f}".format(
                i, xyVal[0][0], xyVal[1][0]
            ),
        )

        # Apply correction to the solution
        xyVal = xyVal + delta()

        # Increment counter
        i = i + 1

    printFrame(
        frame,
        "    {:5d} | {: 13.7f} | {: 13.7f}".format(
            i, xyVal[0][0], xyVal[1][0]
        ),
    )
    printFrame(
        frame,
        "\nThe solution is {}={:.4f} {}={:.4f} after {} iterations".format(
            symbol1, xyVal[0][0], symbol2, xyVal[1][0], i
        ),
    )

    return xyVal

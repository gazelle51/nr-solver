import sympy as sym


def newtonRaphsonSingleVariable(f, symbol, initVal, eps=0.0001):
    """Use the Newton Raphson method to find the solution to a function with
    a single variable.
    
    Args:
        f (str): the function to find the solution of
        symbol (str): symbol for the unknown variable in the function
        initVal (float): initial guess for the solution
        eps (float): epsilon threshold value (default is 0.0001)

    Returns:
        float: Solution to the function
    """

    # Initialisation
    i = 0  # Counter
    xVal = initVal  # Initial guess for x
    xSym = sym.symbols(symbol)  # Symbol used for x
    f = sym.sympify(f)  # Convert function to sympy
    dfdx = sym.diff(f, xSym)  # Function derivative

    def delta():
        """Calculate and return the correction amount."""
        return -f.subs(xSym, xVal).evalf() / dfdx.subs(xSym, xVal).evalf()

    print("\nStarting Newton Raphson Method for a single variable")
    print("\nIteration |       {} (7dp)".format(symbol))
    print("==========================")

    # Start looping
    while abs(delta()) >= eps:
        print("    {:5d} | {: 13.7f}".format(i, xVal))

        # Apply correction to the solution
        xVal = xVal + delta()

        # Increment counter
        i = i + 1

    print("    {:5d} | {: 13.7f}".format(i, xVal))
    print(
        "\nThe solution is {}={:.4f} after {} iterations".format(
            symbol, xVal, i
        )
    )

    return xVal

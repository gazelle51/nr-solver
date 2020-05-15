def newtonRaphsonSingleVariable(x, f, dfdx, eps=0.0001):
    """Use the Newton Raphson method to find the solution to a function with
    a single variable.
    
    Args:
        x (float): initial guess for the solution
        f (function): the function to find the solution of
        dfdx (function): the derivative of the function
        eps (float): epsilon threshold value (default is 0.0001)

    Returns:
        float: Solution to the function
    """

    # Initialisation
    i = 0

    def delta():
        """Calculate and return the correction amount."""
        return -f(x) / dfdx(x)

    print("\nStarting Newton Raphson Method for a single variable")
    print("\nIteration |       x (7dp)")
    print("==========================")

    # Start looping
    while abs(delta()) >= eps:
        print("    {:5d} | {: 13.7f}".format(i, x))

        # Apply correction to the solution
        x = x + delta()

        # Increment counter
        i = i + 1

    print("    {:5d} | {: 13.7f}".format(i, x))
    print("\nThe solution is x=%.4f after %d iterations" % (x, i))

    return x

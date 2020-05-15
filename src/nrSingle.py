# NR Method
def newtonRaphsonSingleVariable(x, f, dfdx, eps=0.0001):
    # Initialisation
    i = 0

    # Delta function, outputs correction amount
    def delta():
        return -f(x) / dfdx(x)

    print("Starting Newton Raphson Method for a single variable")
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

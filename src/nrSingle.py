# NR Method
def newtonRaphsonSingleVariable(x, f, df, eps=0.0001):
    # Initialisation
    delta = f(x) / df(x)
    i = 0

    print("Starting Newton Raphson Method for a single variable")
    print("\nIteration |       x (7dp)")
    print("==========================")

    # Start looping
    while abs(delta) >= eps:
        print("    {:5d} | {: 13.7f}".format(i, x))

        # Calculote delta
        delta = f(x) / df(x)

        # Apply update to the root
        x = x - delta

        # Increment counter
        i = i + 1

    print("    {:5d} | {: 13.7f}".format(i, x))
    print("\nThe value of the root is %.4f after %d iterations" % (x, i))

    return x

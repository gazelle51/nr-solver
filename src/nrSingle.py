# NR Method
def newtonRaphsonSingleVariable(x, f, df, eps=0.0001):
    print("Starting Newton Raphson Method for a single variable")

    delta = f(x) / df(x)
    i = 0

    print("\nIteration |       x (7dp)")
    print("==========================")
    while abs(delta) >= eps:
        print("    {:5d} | {: 13.7f}".format(i, x))

        delta = f(x) / df(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - delta

        i = i + 1

    print("    {:5d} | {: 13.7f}".format(i, x))
    print("\nThe value of the root is %.4f after %d iterations" % (x, i))

import numpy as np

# NR Method
def newtonRaphsonMultiVariable(x, y, f, g, dfdx, dfdy, dgdx, dgdy, eps=0.0001):
    # Jacobian Matrix
    J = np.array([[dfdx(x, y), dfdy(x, y)], [dgdx(x, y), dgdy(x, y)]])

    # Initialisation
    i = 0
    xy = np.array([[x], [y]])

    def delta():
        return np.matmul(
            -np.linalg.inv(J),
            [[f(xy[0][0], xy[1][0])], [g(xy[0][0], xy[1][0])]],
        )

    print("Starting Newton Raphson Method for multiple variables")
    print("\nIteration |       x (7dp) |       y (7dp)")
    print("==========================================")

    # Start looping
    while (np.abs(delta()) >= eps).any():
        print(
            "    {:5d} | {: 13.7f} | {: 13.7f}".format(i, xy[0][0], xy[1][0])
        )

        # Apply update to the root
        xy = xy + delta()

        # Increment counter
        i = i + 1

    print("    {:5d} | {: 13.7f} | {: 13.7f}".format(i, xy[0][0], xy[1][0]))
    print(
        "\nThe solution is x=%.4f y=%.4f after %d iterations"
        % (xy[0][0], xy[1][0], i)
    )

    return x

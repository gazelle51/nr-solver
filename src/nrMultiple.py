import numpy as np

# NR Method
def newtonRaphsonMultiVariable(x, y, f, g, dfdx, dfdy, dgdx, dgdy, eps=0.0001):
    # Initialisation
    i = 0
    xy = np.array([[x, y]]).T

    # Jacobian Matrix
    def J():
        return np.array(
            [
                [dfdx(xy[0][0], xy[1][0]), dfdy(xy[0][0], xy[1][0])],
                [dgdx(xy[0][0], xy[1][0]), dgdy(xy[0][0], xy[1][0])],
            ]
        )

    # Delta function, outputs correction vector
    def delta():
        return np.matmul(
            -np.linalg.inv(J()),
            np.array([[f(xy[0][0], xy[1][0])], [g(xy[0][0], xy[1][0])]]),
        )

    print("Starting Newton Raphson Method for multiple variables")
    print("\nIteration |       x (7dp) |       y (7dp)")
    print("==========================================")

    # Start looping
    while (np.abs(delta()) >= eps).any():
        print(
            "    {:5d} | {: 13.7f} | {: 13.7f}".format(i, xy[0][0], xy[1][0])
        )

        # Apply correction to the solution
        xy = xy + delta()

        # Increment counter
        i = i + 1

    print("    {:5d} | {: 13.7f} | {: 13.7f}".format(i, xy[0][0], xy[1][0]))
    print(
        "\nThe solution is x=%.4f y=%.4f after %d iterations"
        % (xy[0][0], xy[1][0], i)
    )

    return x

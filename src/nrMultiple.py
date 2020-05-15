import numpy as np


def newtonRaphsonTwoVariables(x, y, f, g, dfdx, dfdy, dgdx, dgdy, eps=0.0001):
    """Use the Newton Raphson method to find the solution to two simultaneous 
    equations with two variables.
    
    Args:
        x (float): initial guess for the x value of the solution
        y (float): initial guess for the y value of the solution
        f (function): the first function to find the solution of
        g (function): the second function to find the solution of
        dfdx (function): the derivative of the first function wrt x
        dfdy (function): the derivative of the first function wrt y
        dgdx (function): the derivative of the second function wrt x
        dgdy (function): the derivative of the second function wrt y
        eps (float): epsilon threshold value (default is 0.0001)

    Returns:
        float: Solution to the problem
    """

    # Initialisation
    i = 0
    xy = np.array([[x, y]]).T

    def J():
        """Calculate and return the Jacobian matrix."""

        return np.array(
            [
                [dfdx(xy[0][0], xy[1][0]), dfdy(xy[0][0], xy[1][0])],
                [dgdx(xy[0][0], xy[1][0]), dgdy(xy[0][0], xy[1][0])],
            ]
        )

    def delta():
        """Calculate and return the correction vector."""

        return np.matmul(
            -np.linalg.inv(J()),
            np.array([[f(xy[0][0], xy[1][0])], [g(xy[0][0], xy[1][0])]]),
        )

    print("\nStarting Newton Raphson Method for multiple variables")
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

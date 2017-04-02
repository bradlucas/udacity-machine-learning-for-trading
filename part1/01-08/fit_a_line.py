"""Fit a line to a given set of data using optimization."""

import pandas as pda
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error(line, data): # error function
    """Compute the error between a give line model and the observed data.

    Parameters
    ----------
    line: tuple/list/array (C0, C1) where C0 is the slope and C1 is the Y-intercept
    data: 2D array where each row is a point (x, y)

    Return error value as a single real value.
    """
    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err


def fit_line(data, error_fnc):
    """Fit a line to a given set of data, using a supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_fnc: function that computes the error between a line and the observed data

    Returns a line that minimizes the error function.
    """
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])])  # slope = 0, intercept = mean(y value)

    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")

    # Call the optimzer to minimize the error function
    results = spo.minimize(error_fnc, l, args=(data,), method='SLSQP', options={'disp': True})
    return results.x


def test_run():
    # Define original line
    l_orig = np.float32([4, 2])     # y = mx + b, y = 4x + b
    print "Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

    # Generate noisy data point
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)            # add noise to original data
    data = np.asarray([Xorig, Yorig + noise]).T              
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit a line to this data
    l_fit = fit_line(data, error)
    print "Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1])
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label="Fitted line")
    
    # Add a legend and show plot
    plt.title("Fit a line")
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()

"""Fit a polynomial line to a given set of data using optimization."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):
    """Compute the error between the given polynomial and the observed data.

    parameters
    ----------
    c: numpy.ploly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point (x, y)

    Return error value as a single real value.
    """
    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_fnc, degree=3):
    """Fit a polynomial to given data, using a supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (X, Y)
    error_fnc: function that computes the error between the polynomial and the observed data

    Returns the polynomial that minimizes the error function.
    """
    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype = np.float32))

    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")

    # Call the optimzer to minimize the error function
    results = spo.minimize(error_fnc, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(results.x)


def test_run():
    # @see https://discussions.udacity.com/t/where-can-i-find-the-code-lines-not-shown-in-class/47593
    # Fitting Higher Order Polynomials
    noise_sigma = 3.0
    Cguess = np.poly1d(np.array([1.5, -10, -5, 60, 50], dtype = np.float32))
    print Cguess
    x = np.linspace(-5, 5, 21)
    y = np.polyval(Cguess, x)
    noise = np.random.normal(0, noise_sigma, y.shape)
    print noise
    data = np.asarray([x, y + noise]).T
    fitpoly = fit_poly(data, error_poly)
    print fitpoly
    plt.plot(x, y, 'b-', label = 'Original Line Approx')
    plt.plot(data[:, 0], data[:, 1], 'go', label = 'Data Points')
    plt.plot(data[:, 0], np.polyval(fitpoly, data[:, 0]), 'r--', label = 'Fitted Line')
    plt.legend(loc = 'upper right')
    plt.show()


if __name__ == "__main__":
    test_run()

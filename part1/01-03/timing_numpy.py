import numpy as np
import time


def manual_mean(arr):
    """Compute mean (average) of all elements in the given 2D array"""
    sum = 0
    for i in xrange(0, arr.shape[0]):
        for j in xrange(0, arr.shape[1]):
            sum += arr[i, j]
    return sum / arr.size

def numpy_mean(arr):
    return arr.mean()

def how_long(fn, *args):
    t0 = time.time()
    # Call function via pointer
    result = fn(*args)
    t1 = time.time()
    return result, t1 - t0


def test_run():
    nd1 = np.random.random((1000, 10000))

    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    
    print "\n"
    print "Manual: {:.6} ({:.3f} secs)".format(res_manual, t_manual)
    print "Numpy : {:.6} ({:.3f} secs)".format(res_numpy, t_numpy)
    print "\n"

    # Are the results close enough
    assert abs(res_manual - res_numpy) <= 10e-6, "Results are not equal"

    # Calc difference
    diff = t_manual / t_numpy
    print "NumPy is ", diff, "times faster than manual for loops"


if __name__ == "__main__":
    test_run()




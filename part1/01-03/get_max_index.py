import numpy as np


def get_max_index(a):
    """Return the indx of the maximum value in a given 1D array."""
    return a.argmax()


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)
    print "Array:\n", a

    print "Maxium value: ", a.max()
    print "Index of max.:", get_max_index(a)


if __name__ == "__main__":
    test_run()

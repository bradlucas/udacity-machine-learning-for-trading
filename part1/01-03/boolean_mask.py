import numpy as np


def test_run():
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print a

    mean = a.mean()
    print mean

    # Print all the elements which are less than the mean
    print a[a < mean]

    # Replace all the values which are less than the mean with the mean
    a[a < mean] = mean
    print a


if __name__ == "__main__":
    print "\n"
    test_run()

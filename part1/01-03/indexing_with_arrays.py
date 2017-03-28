import numpy as np


def test_run():
    a = np.random.rand(5)
    print a

    indices = np.array([1, 1, 2, 3])

    print a[indices]


if __name__ == "__main__":
    print "\n"
    test_run()

import numpy as np


def test_run():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 04, 50)])
    print a

    print "\n"
    print a + 2

    print "\n"
    print a / 2.0

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print "\n"
    print a + b

    print "\n"
    print a * b

    print "\n"
    print a / b




if __name__ == "__main__":
    print "\n"
    test_run()

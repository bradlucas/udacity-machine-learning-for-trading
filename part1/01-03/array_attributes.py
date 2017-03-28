import numpy as np


def test_run():
    a = np.random.random((5, 4))
    print a.shape
    print a.shape[0], "rows"
    print a.shape[1], "columns"
    print a.size, "elements"
    print a.dtype


if __name__ == "__main__":
    test_run()

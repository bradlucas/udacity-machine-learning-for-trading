import numpy as np


def test_run():
    np.random.seed(693)   # seed the random number generator
    a = np.random.randint(0, 10, size=(5,4))  # 5x4 random integers in [0, 10]
    print "Array:\n", a

    # Sum all numbers in the array
    print "Sum:\n", a.sum()

    # Sum in direction. Along row or column. this is called axis
    # axis = 0 columns
    # axis = 1 rows

    print "Sum of each column is:\n", a.sum(axis=0)

    print "Sum of each row is:\n", a.sum(axis=1)

    # Min of each column
    print "Minimum of each column is: \n", a.min(axis=0)
    
    print "Maxium of each row is:\n", a.max(axis=1)

    # Mean of all the elements
    print "Mean of the array elements is:\n", a.mean();


if __name__ == "__main__":
    test_run()

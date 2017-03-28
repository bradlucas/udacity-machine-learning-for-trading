import numpy as np


def test_run():
    # Genrate an array full of random numbgers, uniformly sampled from [0.0, 1.0]
    # Results are from the “continuous uniform” distribution over the stated interval. To sample Unif[a, b), b > a multiply the output of random_sample by (b-a) and add a:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random.html
    print np.random.random((3,2))

    # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html
    print np.random.rand(3,2)

    # Draw random samples from a normal (Gaussian) distribution.
    print np.random.normal(size=(2, 3))    # "Standard normal" (mean = 0, s.d. = 1)


    print np.random.normal(50, 10, size=(2, 3))    # "Standard normal" (mean = 0, s.d. = 1)

    # Random integers
    print np.random.randint(10)                   # single integer in [0-10]
    print np.random.randint(0, 10)                # save as previous
    print np.random.randint(0, 10, size=5)        # 5 random integers as a 1D array
    print np.random.randint(0, 10, size=(2, 3))   # 2x3 array of random integers



if __name__ == "__main__":
    test_run()

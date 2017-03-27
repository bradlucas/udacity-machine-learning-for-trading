import pandas as pd

filename = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/AAPL.csv'


def test_run():
    print filename
    """Function called by Test Run."""
    df = pd.read_csv(filename)
    print df[10:21]    # print rows 10..20


if __name__ == "__main__":
    test_run()

import pandas as pd

filename = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/AAPL.csv'

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.tail.html


def test_run():
    print filename
    """Function called by Test Run."""
    df = pd.read_csv(filename)
    # TODO: Print last 5 rows of the data frame
    # print df.tail(5)
    print df.head(5)


if __name__ == "__main__":
    test_run()

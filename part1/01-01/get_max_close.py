import pandas as pd


data_dir = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/'


symbols = ['AAPL', 'IBM']


def get_data_file(symbol):
    rtn = data_dir + "{}.csv"
    return rtn.format(symbol)


def get_max_close(symbol):
    filename = get_data_file(symbol)
    df = pd.read_csv(filename)
    return df['Close'].max()


def test_run():
    for symbol in symbols:
        print "Max close"
        print symbol, get_max_close(symbol)


if __name__ == "__main__":
    test_run()

import pandas as pd
import matplotlib.pyplot as plt

data_dir = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/'


def get_data_file(symbol):
    rtn = data_dir + "{}.csv"
    return rtn.format(symbol)


def test_run():
    filename = get_data_file('IBM')
    df = pd.read_csv(filename)
    df['High'].plot()
    plt.show()


if __name__ == "__main__":
    test_run()

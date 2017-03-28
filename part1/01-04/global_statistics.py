import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    data_dir = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/{}.csv'
    return os.path.join(base_dir, data_dir.format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    print symbols
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, 
                                  usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    start_date = '2010-01-01'
    end_date = '2012-12-31'
    dates = pd.date_range(start_date, end_date)

    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']

    df = get_data(symbols, dates)
    # plot_data(df)

    # computer global statistics for each stock
    print "Mean\n", df.mean()       # Average
    print "Median\n", df.median()   # Value in the middle when sorted
    print "Std\n", df.std()         # Square root of variance. Measure of deviation from the mean



if __name__ == '__main__':
    print "main"
    test_run()

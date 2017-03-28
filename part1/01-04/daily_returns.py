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


def plot_data(df, title="Stock prices", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    plt.show()



def compute_daily_returns(df):
    """Compute and return the daily return values.."""
    # (value[t] / value[t-1]) - 1
    daily_returns = df.copy()
    # compute daily returns for row 1 onwards, note the .values
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0   # set daily returns for row 0 to 0
    return daily_returns


# Using Pandas
def compute_daily_returns(df):
    """Compute and return the daily return values.."""
    # (value[t] / value[t-1]) - 1
    rtn = (df/df.shift(1)) - 1
    rtn.ix[0, :] = 0
    return rtn



def test_run():
    start_date = '2012-07-01'
    end_date = '2012-07-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    print daily_returns

    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")



if __name__ == '__main__':
    print "main"
    test_run()



# NOTE: Passes but gives this warning
# FutureWarning: pd.rolling_std is deprecated for Series and will be removed in a future version, replace with 
#     Series.rolling(window=30,center=False).std()
#   return pd.rolling_std(values, window=window)
